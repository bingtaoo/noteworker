from celery import Celery


class WorkTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super(WorkTask, self).on_failure(exc, task_id, args, kwargs, einfo)

    def run(self, *args, **kwargs):
        """The body of the task executed by workers."""
        raise NotImplementedError('Tasks must define the run method.')
