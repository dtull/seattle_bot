import json
import requests

DATA_URL = 'https://data.seattle.gov/resource/y7iv-rz67.json'

def get_data():
    resp = requests.get(DATA_URL)
    txt = resp.text
    data = json.loads(txt)
    return data

def get_urls_for_hood(neighborhoodstr):
    data = get_data()
    mylist =[]
    for item in data:
        if neighborhoodstr.upper() in item['neighborhood'].upper():
            n = item['name']
            try:
                c = item['url']
            except KeyError:
                pass
            mylist.append([n, c])
    return mylist
