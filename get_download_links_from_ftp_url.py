import requests
from bs4 import BeautifulSoup, SoupStrainer

url = "http://dl2.funsaber.net/serial/Friends/"

download_links = []
video_file_extensions = ('mkv', 'mp4', 'mpeg4', 'mov', 'avi')

def recursiveUrl(url, depth):
        if depth == 5:
                return url
        elif url.endswith(video_file_extensions):
                download_links.append(url)
                return
        else:
                page = requests.get(url)
                for link in BeautifulSoup(page.text, parse_only=SoupStrainer('a'), features="html.parser"):
                        if (link.has_attr('href') and link.text != '../'):
                                recursiveUrl(url + link['href'], depth + 1)

def getLinks(url):
        page = requests.get(url)
       
        for link in BeautifulSoup(page.text, parse_only=SoupStrainer('a'), features="html.parser"):
                if (link.has_attr('href') and link.text != '../'):
                        recursiveUrl(url + link['href'], 0)
        return download_links

if __name__ == '__main__':
        getLinks(url)
        for download_link in download_links:
                print('\n')
                print(download_link)