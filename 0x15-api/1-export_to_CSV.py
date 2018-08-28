#!/usr/bin/python3
# Gathers data from an API

import csv
import requests
import sys


def export_csv():
    emp_id = int(sys.argv[1])
    resp = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)).json()
    emp_name = resp['name']
    
    todo_resp = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    download_dir = "{}.csv".format(sys.argv[1])
    with open(download_dir, "w", newline='') as csvfile:
        f = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todo_resp:
            if todo['userId'] == emp_id:
                completed = todo['completed']
                title = todo['title']
                f.writerow([emp_id, emp_name, completed, title])

if __name__ == '__main__':
    export_csv()
