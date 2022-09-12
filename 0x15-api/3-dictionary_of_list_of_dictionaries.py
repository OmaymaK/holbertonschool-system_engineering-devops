#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests


if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    udict = {}

    for user in users:
        td = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                          .format(str(user.get('id')))).json()
        udict[str(user.get('id'))] = []
        for todo in td:
            tds = {"username": user.get('username'),
                   "task": todo.get('title'),
                   "completed": todo.get('completed')}
            udict[str(user.get('id'))].append(tds)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(udict, file)
