from __future__ import absolute_import, unicode_literals

from .celery import app
import time
import random

@app.task
def add(x, y):
    sleep_time = random.randint(0, 5)
    time.sleep(sleep_time)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)