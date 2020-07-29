## Broker settings.
broker_url = 'amqp://guest:guest@rabbitmq:5672//'

# List of modules to import when the Celery worker starts.

result_backend = 'rpc://guest:guest@rabbitmq:5672/'

result_expires=3600