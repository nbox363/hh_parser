import requests

from celery import Celery


app = Celery('tasks', backend='rpc://', broker='pyamqp://')


@app.task
def get_page(page=0):
    params = {
        'text': 'Python Junior',
        'area': 1,
        'page': page,
        'per_page': 100
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.json()
    return data


@app.task
def get_data(data):
    key_skills = ''
    for skill in data['key_skills']:
        key_skills += str(skill['name'] + ', ')
    name = data['name']
    try:
        salary = data['salary']['to']
    except TypeError:
        try:
            salary = data['salary']['from']
        except TypeError:
            salary = 0
    description = data['description']
    url = data['area']['url']
    return key_skills, name, salary, description, url
