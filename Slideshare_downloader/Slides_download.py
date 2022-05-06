import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
import re

URL = input("enter a slideshare link :")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

slide_images = []
for link in soup.find_all("img", {"class": "slide-image"}):
    actual_link = str(link.get("srcset")).split(",")[2].split()[0]
    # print(actual_link)
    slide_images.append(actual_link)


for link in slide_images:
 
    pattern = "(?<=/\d\d/)(.*)(?=\?)"
    filename = re.search(pattern, link).group(1)


    response = requests.get(link)
    file = open(filename, "wb")
    file.write(response.content)
    file.close()
    
    print(filename,"saved")
    




