#!/usr/bin/python3
"""
Script to gather data from an API and display TODO list progress
for a given employee ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
    else:
        employee_id = int(argv[1])

        # Fetch user information
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate TODO list progress
        total_tasks = len(todo_data)
        completed_tasks = sum(task["completed"] for task in todo_data)

        # Display information
        print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
        for task in todo_data:
            if task["completed"]:
                print("\t {}".format(task["title"]))
