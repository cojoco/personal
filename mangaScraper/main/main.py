import requests
import shutil
from bs4 import BeautifulSoup
from zipfile import ZipFile
import glob
import os

def pad(number):
    if number < 10:
        return '0'+str(number)
    else:
        return str(number)

firstPage = str(raw_input("Please enter the URL of the first page (including trailing slash): "))

images = []

url = firstPage

pageNumber = 2

while True:
    resp = requests.get(url)
    if (resp.status_code == 404):
        break
    soup = BeautifulSoup(resp.text, 'lxml')
    image = soup.find(id="image")["src"]
    images.append(image)
    url = firstPage + str(pageNumber) + '.html'
    pageNumber += 1

print str(pageNumber-2) + " pages found."

for i,image in enumerate(images):
    with open("/home/connor/Documents/comic/" + pad(i+1) + ".jpg", 'w') as file:
        page = requests.get(image, stream=True)
        shutil.copyfileobj(page.raw, file)

print "Image files written"

with ZipFile('/home/connor/Documents/deathnote.cbz', 'w') as myZip:
    for filename in sorted(glob.iglob('/home/connor/Documents/comic/*')):
        myZip.write(filename)
        os.remove(filename)
    myZip.close()

print "Zip file written."

print "Scrape complete."