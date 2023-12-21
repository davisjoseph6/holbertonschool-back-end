#!/usr/bin/python3
"""
Script to gather data from an API, display TODO list progress,
and export data in CSV format for a given employee ID.
"""

import requests
import csv
from sys import argv

def fetch_user_info(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    return user_data.get("id"), user_data.get("name")

def fetch_todo_list(employee_id):
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    return todo_data

def calculate_progress(todo_data):
    completed_tasks = sum(task["completed"] for task in todo_data)
    return completed_tasks, len(todo_data)

def display_information(employee_name, completed_tasks, total_tasks, todo_data):
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        print(f'\t{task["completed"]},{task["title"]}')
    return

def export_to_csv(user_id, employee_name, todo_data):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            csv_writer.writerow([user_id, employee_name, str(task["completed"]), task["title"]])
    print(f'Data exported to {filename}')
    return

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print(f"Usage: {argv[0]} employee_id")
    else:
        employee_id = int(argv[1])

        user_id, employee_name = fetch_user_info(employee_id)
        todo_data = fetch_todo_list(employee_id)
        completed_tasks, total_tasks = calculate_progress(todo_data)

        display_information(employee_name, completed_tasks, total_tasks, todo_data)
        export_to_csv(user_id, employee_name, todo_data)

