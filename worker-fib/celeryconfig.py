## Broker settings.
broker_url = 'amqp://guest:guest@rabbitmq:5672//'

# List of modules to import when the Celery worker starts.
imports = ('worker-fib.tasks',)

task_routes = {
    'worker-fib.*': {'queue': 'fib'}
}

result_backend = 'rpc://guest:guest@rabbitmq:5672/'

result_expires=3600