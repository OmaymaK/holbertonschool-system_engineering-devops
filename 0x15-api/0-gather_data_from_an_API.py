#!/usr/bin/python3
"""Returns information about TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(argv[1]))
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}/"
                        .format(argv[1]))
    todos = todos.json()
    user = user.json()
    done = []

    for todo in todos:
        if todo.get('completed'):
            done.append(todo)
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(done), len(todos)))
    for todo in done:
        print("\t {}".format(todo.get('title')))
