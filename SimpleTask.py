from celery import Celery
import time
from celery.utils.log import get_task_logger

app = Celery(main="one", broker="amqp://guest:guest@0.0.0.0:5672", backend="rpc://")
logger = get_task_logger(__name__)

# change configurations
app.conf.update(
    task_time_limit=60,
    task_soft_time_limit=50,
    worker_concurrency=3,
    worker_perfetch_multiplier=1,
    task_ignore_result=False,
    task_always_eager=False,
    task_ack_late=False,
)


@app.task(name="one.add", task_time_limit=5)
def add(a, b):
    time.sleep(10)
    return a + b


@app.task(name="one.div", bind=True, default_retry_delay=100)
def div(self, a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Zero div error...")
        self.retry(countdown=5, max_retires=2)
    except Exception:
        logger.info("Sorry...")
        # delay= 100 and max_retires=3(default value)
        self.retry()
