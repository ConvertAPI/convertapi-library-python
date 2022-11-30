import convertapi

from .task import Task
from .result import Result

def convert(to_format, params, from_format = None, timeout = None):
    task = Task(from_format, to_format, params, timeout = timeout)
    return task.run()


def user(timeout = None):
    return convertapi.client.get('user', timeout = timeout)


def async_convert(to_format, params, from_format = None, timeout = None):
    task = Task(from_format, to_format, params, timeout = timeout, is_async = True)
    return task.run()


def async_poll(job_id):
    response = convertapi.client.get('async/job/%s' % job_id)
    return Result(response)
