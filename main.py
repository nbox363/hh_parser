import requests
import json
import os


def get_page(page=0):
    params = {
        'text': 'Python Junior',
        'area': 1,
        'page': page,
        'per_page': 100
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode() # str
    return data


for page in range(1):
    js_obj = json.loads(get_page(page)) # dict
    for v in js_obj['items']:
        req = requests.get(v['url'])
        data = req.content.decode()
        req.close()
        fileName = 'vacancies/{}.json'.format(v['id'])
        f = open(fileName, mode='w', encoding='utf8')
        f.write(data)
        f.close()

    


