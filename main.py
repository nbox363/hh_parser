import requests
import sqlite3
from tasks import get_page, get_data


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


def main():
    cur, conn = connect_db()
    for page in range(1):
        vacancies_from_page = get_page.delay(page)
        vacancies = vacancies_from_page.get(timeout=0)
        for vacancy in vacancies['items']:
            row_data = requests.get(vacancy['url']).json()
            d = get_data.delay(row_data)
            data = d.get(timeout=0)
            save_in_db(*data, cur=cur, conn=conn)
    conn.close()


if __name__ == "__main__":
    main()
