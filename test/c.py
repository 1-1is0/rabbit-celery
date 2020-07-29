from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery()

app.config_from_object('test.celeryconfig')

# Optional configuration, see the application user guide.
# app.conf.update(
#         task_routes = {
#         'worker.tasks.add': {'queue': 'add_queue'},
#     },
# )

if __name__ == '__main__':
    app.start()