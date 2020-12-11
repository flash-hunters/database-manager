import math
import re


def getNumberOfPages(page):
    text = page.p.string
    text_data = re.split('\s', text)
    total = text_data[0]
    size = 50
    return int(math.ceil(float(total) / size))


def parse(item, url):
    mosaic = {}

    text = item.td.b.string
    text_data = re.split('[\s\[]', text)
    # avoid mosaics with unknown IDs
    if '?' in text_data[0]:
        return None
    id_data = text_data[0].split('_')
    mosaic['id'] = "{}_{:02d}".format(id_data[0], int(id_data[1]))
    # no score if unknown
    if '?' not in text_data[2]:
        mosaic['score'] = int(text_data[2])

    text = item.font.contents[2]
    text_data = re.split('\(|(\s-\s)|\)', text)
    mosaic['area'] = text_data[2]
    if len(text_data) >= 7:
        mosaic['subarea'] = text_data[4]

    text = (item.font.contents[6])[1:]
    mosaic['state'] = text

    img = item.findAll('img')
    text = img[0]['src']
    mosaic['img1_src'] = url + text
    if len(img) > 2:
        text = img[2]['src']
        mosaic['img2_src'] = url + text
    if len(img) > 3:
        text = img[3]['src']
        mosaic['img3_src'] = url + text

    img = (item.findAll('td'))[1].findAll('a')
    if len(img) > 0:
        text = img[0]['href']
        mosaic['photo_src'] = url + text

    return mosaic
