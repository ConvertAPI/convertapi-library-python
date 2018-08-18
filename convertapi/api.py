from .task import Task

def convert(to_format, params, from_format = None, timeout = None):
    task = Task(from_format, to_format, params, timeout = timeout)
    return task.run()
