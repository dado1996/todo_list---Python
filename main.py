import os.path
import json

from tasks.create import create
from tasks.edit import edit
from tasks.delete import delete
from tasks.list import list
from tasks.check import check_task

# File used for storing tasks after sessions
FILE = "tmp/tasks.txt"

tasks = []
if (os.path.isfile(FILE)):
    # Tasks are loaded in the array if the file isn't empty
    fout = open(FILE, 'r')
    raw_tasks = fout.read()

    if (len(raw_tasks) > 0):
        tasks = json.loads(raw_tasks.replace("'", '"'))

while True:
    # User selects the action
    try:
        action = input("Select the action you want to perform:\n"
                    "1. Create a task\n2. Edit a task\n"
                    "3. Delete a task\n4. List all tasks\n"
                    "5. Check/Uncheck a task\n"
                    "0. End the program\n")
        
        # Checks that the action is valid
        if not action.isnumeric():
            print("Invalid action\n")
            continue

        action = int(action)
        if action == 1:
            # Creates a new task
            task_name = input("Insert the name of the task: ")
            create(tasks, task_name)
            list(tasks)
            print("\n")
        elif action == 2:
            # Edits an existing task
            task_name = input("Insert the name of the task you want to edit: ")
            new_task_name = input("Insert the new name of the task: ")
            edit(tasks, task_name, new_task_name)
            list(tasks)
        elif action == 3:
            # Deletes a task
            task_name = input("Insert the name of the task you want to delete: ")
            delete(tasks, task_name)
            list(tasks)
        elif action == 4:
            # Displays all tasks
            print("List of saved tasks")
            list(tasks)
        elif action == 5:
            # Checks/Unchecks a task
            task_name = input("Insert the name of the task you want to check/uncheck: ")
            check_task(tasks, task_name)
            list(tasks)
        elif action == 0:
            # Saves the tasks in the file and ends the program
            fout = open(FILE    , 'w')
            fout.write(json.dumps(tasks))
            print("Program ended")
            break;
    except ValueError:
        print('There was an error')
    except Exception:
        print('There was an exception')