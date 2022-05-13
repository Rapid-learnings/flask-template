from celery import Celery
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

celery = None


def make_celery(app):
    if app.config['CELERY_RESULT_BACKEND'] is None:
        raise Exception('CELERY_RESULT_BACKEND is not set')

    if app.config['CELERY_BROKER_URL'] is None:
        raise Exception('CELERY_BROKER_URL is not set')


    global celery
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery

