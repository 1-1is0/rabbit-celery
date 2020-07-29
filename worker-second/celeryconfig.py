## Broker settings.
broker_url = 'amqp://guest:guest@rabbitmq:5672//'

# List of modules to import when the Celery worker starts.
imports = ('worker-second.tasks',)

task_routes = {
    'worker-second.tasks.add': {'queue': 'second'}
}

result_backend = 'rpc://guest:guest@rabbitmq:5672/'

result_expires=3600