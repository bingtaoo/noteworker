from celery import Celery


class WorkApp(Celery):
    def __init__(self, *args, **kwargs):
        super(WorkApp, self).__init__(*args, **kwargs)

