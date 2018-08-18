import convertapi

from .task import Task

def convert(to_format, params, from_format = None, timeout = None):
    task = Task(from_format, to_format, params, timeout = timeout)
    return task.run()

def user(timeout = None):
    return convertapi.client.get('user', timeout = timeout)
