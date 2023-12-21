#!/usr/bin/python3
"""
extended your Python script to export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    """ getting todo list of users from an api  """
    n = sys.argv[1]
    resUser = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
    response = resUser.json()
    resTask = requests.get('https://jsonplaceholder.typicode.com/todos')
    responseTask = resTask.json()
    done = 0
    total = 0
    doneTask = []
    for task in responseTask:
        if task["userId"] == int(n):
            if task["completed"] is True:
                doneTask.append(task["title"])
                done += 1
            else:
                total += 1

    total += done

    print(f"Employee {response['name']} is done with tasks({done}/{total}):")
    for task in doneTask:
        print(f"\t {task}")

    filename = f"{n}.csv"
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for task in responseTask:
            if task['userId'] == int(n):
                rows = []
                USER_ID = str(task["userId"])
                USERNAME = response["username"]
                TASK_COMPLETED_STATUS = str(task["completed"])
                TASK_TITLE = task['title']

                f.write('"{}","{}","{}","{}"\n'.format(
                    USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE))
