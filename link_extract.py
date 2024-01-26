from bs4 import BeautifulSoup
import re
import urllib.request


def link_fetch():
    with open("Data_Extraction/raw_html.txt",'r') as fh:
        html_text = fh.read()

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find all links that match the specified pattern
    pattern = re.compile(r"https://www\.nirfindia\.org/nirfpdfcdn/2022/graph/Engineering/.*\.png")
    links = soup.find_all('a', href=pattern)
    return links




def return_links(object):
    image_links=[]
    for i in object:
        image_links.append(i['href'])
    return image_links


list_of_links = return_links(link_fetch())


def cropped_file_names():
    names = []
    for i in list_of_links:
        names.append('c_'+i[60:])
    return names

def download_images(links):
    for link in links:
        f_name = link[60:]
        urllib.request.urlretrieve(link, f"Images/2022_Engineering/{f_name}")  

download_images(list_of_links)
