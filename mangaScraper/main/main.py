import requests
import shutil
from bs4 import BeautifulSoup

def pad(number):
    if number < 10:
        return '0'+str(number)
    else:
        return str(number)

urls = ['http://www.mangatown.com/manga/death_note/v00/c001/']

for i in xrange(2,53):
    urls.append('http://www.mangatown.com/manga/death_note/v00/c001/' + str(i) + '.html')

images = []

for url in urls:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    image = soup.find(id="image")["src"]
    images.append(image)

for i,image in enumerate(images):
    with open("images/file" + pad(i+1) + ".jpg", 'w') as file:
        page = requests.get(image, stream=True)
        shutil.copyfileobj(page.raw, file)