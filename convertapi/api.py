from .task import Task

def convert(to_format, params, from_format = None, conversion_timeout = None):
    task = Task(from_format, to_format, params, conversion_timeout = conversion_timeout)
    return task.run()
