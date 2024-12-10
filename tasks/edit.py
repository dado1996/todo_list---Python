def edit(tasks, task_name, task_new_name):
    # Searches the id of the dict found by the name
    task_id = tasks.index(next(item for item in tasks if item['name'] == task_name))
    tasks[task_id] = {
        'name': task_new_name,
        'done': False
    }