#!/usr/bin/python3
"""
extended my Python script to export data in the JSON format.
"""

import json
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
        json_file = f"{n}.json"
        final_dict = {}
        final_list = []
        task_list = []
        for task in responseTask:
            if task["userId"] == int(n):
                USER_ID = task["userId"]
                TASK_TITLE = task['title']
                TASK_COMPLETED_STATUS = task["completed"]
                USERNAME = response["username"]

                task_list.append({
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS,
                    "username": USERNAME
                })

                with open(json_file, "w") as jf:
                    json.dump({USER_ID: task_list}, jf)
