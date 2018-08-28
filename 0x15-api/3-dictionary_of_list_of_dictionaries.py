#!/usr/bin/python3
# Gathers data from an API

import json
import requests
import sys


def all_todos():
    resp = requests.\
        get('https://jsonplaceholder.typicode.com/users').\
        json()
    todo_resp = requests.\
        get('https://jsonplaceholder.typicode.com/todos').json()

    all_todos = {}
    for user in resp:
        emp_id = user['id']
        username = user['username']
        all_todos[emp_id] = []
        for todo in todo_resp:
            if todo['userId'] == emp_id:
                todo_dict = {}
                todo_dict['username'] = username
                todo_dict['task'] = todo['title']
                todo_dict['completed'] = todo['completed']
                all_todos[emp_id].append(todo_dict)
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_todos, jsonfile)

if __name__ == '__main__':
    all_todos()
