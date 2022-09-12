#!/usr/bin/python3
"""Records all tasks that are owned by this employee."""
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    todos = todos.json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    user = user.json()
    with open(str(user.get('id'))+".csv", 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user.get('id'), user.get('username'),
                               todo.get('completed'), todo.get('title')))
