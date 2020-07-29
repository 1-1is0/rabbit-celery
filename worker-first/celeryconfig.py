## Broker settings.
broker_url = 'amqp://guest:guest@rabbitmq:5672//'

# List of modules to import when the Celery worker starts.
imports = ('worker-first.tasks',)

task_routes = {
    'worker-first.tasks.add': {'queue': 'first'}
}

result_backend = 'rpc://guest:guest@rabbitmq:5672/'

result_expires=3600