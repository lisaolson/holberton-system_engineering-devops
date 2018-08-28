#!/usr/bin/python3
# Gathers data from an API

import json
import requests
import sys


def export_json():
    emp_id = int(sys.argv[1])
    resp = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)).\
        json()
    username = resp['username']
    todo_resp = requests.\
        get('https://jsonplaceholder.typicode.com/todos').json()

    download_dir = "{}.json".format(sys.argv[1])

    return_data = []
    for todo in todo_resp:
        if todo['userId'] == emp_id:
            todo_dict = {}
            todo_dict['task'] = todo['title']
            todo_dict['completed'] = todo['completed']
            todo_dict['username'] = username
            return_data.append(todo_dict)
    return_dict = {emp_id: return_data}
    with open(download_dir, "w") as jsonfile:
        json.dump(return_dict, jsonfile)

if __name__ == '__main__':
    export_json()
