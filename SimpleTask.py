from celery import Celery
import time

app = Celery(main='one', broker='amqp://guest:guest@0.0.0.0:5672')

@app.task(name='one.add')
def add(a, b):
    time.sleep(10)
    return a + b