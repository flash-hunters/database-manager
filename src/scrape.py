import json
import os
import requests

import bs4

from src.scrape_utils import *

url = 'http://invader.spotter.free.fr/'
page = url + 'listing.php'

data = []

i = 0
numberOfPages = 1
while i < numberOfPages:

    print("Scanning page {}".format(i + 1))

    postData = {'page': i + 1}
    http = requests.post(page, postData)
    if http.status_code != 200:
        exit(1)
    http.encoding = 'utf-8'

    html = http.text
    html = html.replace("<br>", "<br/>")

    soup = bs4.BeautifulSoup(html, "html.parser")

    if i == 0:
        numberOfPages = getNumberOfPages(soup)

    for item in soup.findAll('tr', attrs={"class": "haut"}):
        mosaic = parse(item, url)
        if mosaic is not None:
            data.append(mosaic)

    i = i + 1

data = json.dumps(data, ensure_ascii=False, indent=4)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../out/mosaics.json')
f = open(filename, "w")
f.write(data)
f.close()
