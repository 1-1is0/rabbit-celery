from __future__ import absolute_import, unicode_literals

from celery import Celery
import time
import random

# rabbit_path = 'amqp://guest:guest@rabbitmq:5672/'
# backend = 'amqp://guest:guest@rabbitmq:5672/'
# celeryapp = Celery('test', broker=rabbit_path, backend=backend)
# celeryapp.config_from_object('config.celeryconfig')
celery = Celery()
celery.config_from_object('celeryconfig')

tasks = {
    'worker-fib.tasks.fib': {"queue": "fib", "arg_num": 1},
    'worker-math.tasks.add': {"queue": "math", "arg_num": 2},
    'worker-math.tasks.mul': {"queue": "math", "arg_num": 2},
}

while True:
    print("[.] NEW Tasks are being added")
    result_list = []
    for task_name, info in tasks.items():
        args = [random.randint(1, 50) for i in range(0, info.get('arg_num'))]
        print(f"[.] Send Request to task {task_name} with args {args}")
        result = celery.send_task(task_name, args=args, queue=info.get('queue'))
        result_list.append((task_name, result))
    
    # now that we push 3 task to queues we wait for some seconds and get all of them
    time.sleep(2)
    print()

    for task_name, result in result_list:
    
        print(f"[x] {task_name} result -> {result.get()}")
    print()