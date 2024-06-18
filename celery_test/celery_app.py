from celery import Celery
import celery_test.tasks

app = Celery('celery_test',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
