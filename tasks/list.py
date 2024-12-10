def list(tasks):
    for t in tasks:
        print("%s: %s" % (t['name'], 'Done' if t['done'] else 'Pending'))