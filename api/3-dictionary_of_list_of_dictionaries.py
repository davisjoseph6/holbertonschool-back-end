#!/usr/bin/python3
"""
Extended your Python script to export data in the JSON format.
"""

import json
import requests


if __name__ == "__main__":
    """ getting todo list of users from an api  """
    resUser = requests.get('https://jsonplaceholder.typicode.com/users')
    response = resUser.json()
    resTask = requests.get('https://jsonplaceholder.typicode.com/todos')
    responseTask = resTask.json()

    json_file = "todo_all_employees.json"
    task_list = []
    a_user = []
    all_users = []
    new_dict = {}
    for user in response:
        USER_ID = int(user["id"])
        task_list = []
        for task in responseTask:
            if int(task["userId"]) == USER_ID:
                TASK_TITLE = task['title']
                TASK_COMPLETED_STATUS = task["completed"]
                USERNAME = user["username"]

                task_list.append({
                    "username": USERNAME,
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS
                })
        new_dict[USER_ID] = task_list
        with open(json_file, "w") as jf:
            json.dump(new_dict, jf)
