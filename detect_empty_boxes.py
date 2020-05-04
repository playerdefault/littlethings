# FAI TechTalk POC for Detecting Empty boxes in a PDF document

from pdf2image import convert_from_path
import cv2 as cv2
import numpy as np
import pytesseract
import json
import boto3

#initialize Dynamo DB
dynamoDb = boto3.resource('dynamodb')
table = dynamoDb.Table('TechTalk-LFG')

#initialize S3
s3 = boto3.client('s3')
#id ="4832072d-c44d-464b-9380-9d29980b30e8"
templateID=""

def GetTemplateFileInfo(_id):
	response = table.get_item(Key={'TemplateId': _id})
	item = response['Item']
	#print("GetItem succeeded:",item)
	keys = item.keys() 
	values = item.values() 

def save_pdf_pages(PDF_file, save_dir):
    pages = convert_from_path(pdf_path=PDF_file, dpi=500)

    for page_no, page in enumerate(pages):
        filename = save_dir + "/page_" + str(page_no + 1) + ".jpg"
        page.save(filename, 'JPEG')

def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    
    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top
    # to bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
    key=lambda b : b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

def is_text_present(input_img):
    text = pytesseract.image_to_string(input_img)
    if (text == "" or '.'):
        return False
    else:
        return True

def box_extraction(img_for_box_extraction_path, final_contours):
    img = cv2.imread(img_for_box_extraction_path, 0) # Read the image

    img_bin = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img_bin = 255 - img_bin # Invert the image

    # Defining a kernel length
    vertical_kernel_length = np.array(img).shape[1]//100
    horizontal_kernel_length = np.array(img).shape[0]//100

    # A vertical kernel of (1 x kernel_length), which will detect all the vertical lines from the image
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_kernel_length))
    # A horizontal kernel of (kernel_length x 1), which will help detect all the horizontal lines from the image
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_kernel_length, 1))
    # A kernel of (3 x 3) ones
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Morphological operation to detect vertical lines from an image
    img_temp1 = cv2.erode(img_bin, vertical_kernel, iterations=1)
    vertical_lines_img = cv2.dilate(img_temp1, vertical_kernel, iterations=1)

    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, horizontal_kernel, iterations=1)
    horizontal_lines_img = cv2.dilate(img_temp2, horizontal_kernel, iterations=1)

    # Weighting parameters, this will decide the quality of an image to be added to make a new image
    alpha = 0.5
    beta = 1.0 - alpha

    # This function helps to add 2 images with specific weight parameter to get a third image as simulation of the 2 images
    img_final_bin_addwgtd = cv2.addWeighted(vertical_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin_eroded = cv2.erode(~img_final_bin_addwgtd, kernel, iterations=1)

    # Find contours for the image, which will detect all the boxes
    contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort all the contours by top to bottom
    (contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")

    idx = 0
    for c in contours:
        # Returns the location, width, and height of every contour
        x, y, w, h = cv2.boundingRect(c)
        
        # If the box height is greater than 20, width is greater than 80, then only save it as a box in the cropped folder
        if (w > 50 and h > 20):
            idx += 1
            new_img = img[y:y+h, x:x+w]
            if (is_text_present(new_img) == False):
                contour = {}
                contour["x1"] = x/(np.array(img).shape[1])
                contour["x2"] = (x + w)/(np.array(img).shape[1])
                contour["y1"] = (y + h)/(np.array(img).shape[0])
                contour["y2"] = (y)/(np.array(img).shape[0])
                contour["height"] = h
                contour["width"] = w
                contour_json = json.dumps(contour)
                final_contours.append(contour_json)
    
    return final_contours

def lambda_handler(event, context):

    templateID = event['queryStringParameters']['id']
    PDF_Name = GetTemplateFileInfo(templateID)
    response = s3.get_object(Bucket="techtalk-legalformgeneration", Key="Docs/"+templateID+"/" + PDF_Name + ".pdf", "/tmp/source.pdf")
    
    temp_dir = "/tmp"
    PDF_file = temp_dir + "/source.pdf"

    save_pdf_pages(PDF_file, temp_dir)

    final_contours = []

    pages = convert_from_path(pdf_path=PDF_file, dpi=500)
    for page_no, page in enumerate(pages):
        filename = temp_dir + "/page_" + str(page_no + 1) + ".jpg"
        final_contours = box_extraction(filename, temp_dir, final_contours)

    s3.Bucket("techtalk-legalformgeneration")
    json.dump_s3 = lambda obj, f: s3.Object(key=f).put(Body=json.dumps(obj))
    json.dump_s3(final_contours, "blank_boxes.json")

    return {
		'statusCode':200,
		'body':json.dumps(final_contours),
		'headers':{	
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': event['headers']['origin'],
				'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
		}
	}
