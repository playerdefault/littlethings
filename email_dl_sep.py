# This program separates a list of semi-colon separated emails from a text file
# and prints out the number of emails

path = input(str("Enter the relative path of the file with the DL List: "))
DLListInputFile = open(path, 'r')
DLInput = DLListInputFile.read() 
numberOfEmails = 0
for char in DLInput:
	if(char==";"):
		numberOfEmails += 1
print("The number of emails is: " + str(numberOfEmails))
