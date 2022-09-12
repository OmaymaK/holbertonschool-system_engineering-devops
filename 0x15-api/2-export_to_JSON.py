#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1])).json()

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()

    udict = {str(user.get('id')): []}
    for todo in todos:
        td = {"task": todo.get('title'),
              "completed": todo.get('completed'),
              "username": user.get('username')}
        udict[str(user.get('id'))].append(td)

    with open(str(user.get('id'))+".json", 'w') as file:
        json.dump(udict, file)
