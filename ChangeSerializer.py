from celery import Celery
from Person import Persons

# celery -A ChangeSerializer worker -l info

app = Celery(main='ChangeSerializer', broker="amqp://guest:guest@0.0.0.0:5672", 
             backend='rpc://')

app.conf.update(
    task_serializer= 'pickle',
    result_serializer = 'pickle',
    accept_content = ['application/x-python-serialize']
)

@app.task(bind=True)
def call(self, person):
    # check content type.
    # print(self.result)
    return person.show()
