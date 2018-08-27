#!/usr/bin/python3
# Gathers data from an API

import requests
import sys


TASK_TITLE = ""
TOTAL_NUMBER_OF_TASKS = 0
NUMBER_OF_DONE_TASKS = 0

emp_id = int(sys.argv[1])
resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(emp_id))
data = resp.json()
emp_name = data['name']

todo_resp = requests.get('https://jsonplaceholder.typicode.com/todos')
todo_data = todo_resp.json()
for todo in todo_data:
    if todo['userId'] == emp_id:
        TOTAL_NUMBER_OF_TASKS += 1
        if todo['completed'] == True:
            NUMBER_OF_DONE_TASKS += 1

EMPLOYEE_NAME = emp_name

print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

for todo in todo_data:
    if todo['userId'] == emp_id:
        print('\t {}'.format(todo['title']))
