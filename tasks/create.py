def create(tasks, task_name):
    # Appends a new task to the task list with the task_name
    tasks.append({
        'name': task_name,
        'done': False,
    })