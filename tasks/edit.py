def edit(tasks, id, name):
    tasks[id] = {
        'name': name,
        'done': False
    }