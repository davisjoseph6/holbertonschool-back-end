#!/usr/bin/python3
"""
Script to gather data from an API, display TODO list progress,
and export data to CSV for a given employee ID.
"""

import requests
import csv
from sys import argv

def fetch_user_information(employee_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    return user_data.get("id"), user_data.get("name")

def fetch_todo_list(employee_id):
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    return todo_data

def calculate_progress(todo_data):
    completed_tasks = sum(task["completed"] for task in todo_data)
    return completed_tasks

def export_to_csv(employee_id, employee_name, todo_data):
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
    else:
        employee_id = int(argv[1])

        # Fetch user information
        user_id, employee_name = fetch_user_information(employee_id)

        # Fetch TODO list
        todo_data = fetch_todo_list(employee_id)

        # Calculate TODO list progress
        completed_tasks = calculate_progress(todo_data)

        # Display information
        print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, len(todo_data)))
        for task in todo_data:
            if task["completed"]:
                print("\t {}".format(task["title"]))

        # Export to CSV
        export_to_csv(user_id, employee_name, todo_data)
        print("Data exported to {}.csv".format(employee_id))

