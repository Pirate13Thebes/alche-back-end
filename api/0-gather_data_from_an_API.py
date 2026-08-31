#!/usr/bin/python3
"""Gather employee TODO data from an API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    completed = [
        task for task in todos
        if task["completed"]
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"],
            len(completed),
            len(todos)
        )
    )

    for task in completed:
        print("\t {}".format(task["title"]))
