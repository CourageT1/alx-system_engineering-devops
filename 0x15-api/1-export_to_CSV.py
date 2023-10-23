#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import requests
import csv
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_users = "https://jsonplaceholder.typicode.com/users/{}"
    .format(employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"
    .format(employee_id)

    try:
        user_response = requests.get(url_users)
        todos_response = requests.get(url_todos)

        user_data = user_response.json()
        todos_data = todos_response.json()

        csv_file_name = "{}.csv".format(employee_id)

        with open(csv_file_name, mode='w', newline='') as csv_file:
            fieldnames =
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for task in todos_data:
                writer.writerow({
                    "USER_ID": user_data["id"],
                    "USERNAME": user_data["username"],
                    "TASK_COMPLETED_STATUS": task["completed"],
                    "TASK_TITLE": task["title"]
                })

        print("Data exported to {}".format(csv_file_name))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
