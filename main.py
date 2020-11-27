import requests
import sqlite3


def connect_db():
    conn = sqlite3.connect('vacancies.db')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE vacancies(key_skills, name, salary, description, url)')
    return cur, conn


def save_in_db(*data, cur, conn):
    cur.executemany('INSERT INTO vacancies(key_skills, name, salary, description, url) \
                   VALUES(?, ?, ?, ?, ?)', [data])
    conn.commit()


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


def main():
    cur, conn = connect_db()
    for page in range(3):
        vacancies_from_page = get_page(page)
        for vacancy in vacancies_from_page['items']:
            row_data = requests.get(vacancy['url']).json()
            data = get_data(row_data)
            save_in_db(*data, cur=cur, conn=conn)
    conn.close()


if __name__ == "__main__":
    main()
