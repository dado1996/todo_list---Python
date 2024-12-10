def delete(tasks, task_name):
    # Searches the id of the dict found by the name
    task_id = tasks.index(next(item for item in tasks if item['name'] == task_name))
    del tasks[task_id] # Deletes the task