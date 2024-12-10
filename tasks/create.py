def create(tasks, task_name):
    tasks.append({
        'name': task_name,
        'done': False,
    })