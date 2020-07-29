from __future__ import absolute_import, unicode_literals

import time
from .celery import app
from .fib import fib_calc

@app.task
def fib(a):
    if a > 30:
        return "-1"
    return fib_calc(a)
