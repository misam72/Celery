from celery import Celery, signals
import time
from celery.utils.log import get_task_logger

app = Celery(
    main="SimpleTask", broker="amqp://guest:guest@0.0.0.0:5672", backend="rpc://"
)
logger = get_task_logger(__name__)

# change configurations(method 1)
# app.conf.update(
#     task_time_limit=60,
#     task_soft_time_limit=50,
#     worker_concurrency=3,
#     worker_perfetch_multiplier=1,
#     task_ignore_result=False,
#     task_always_eager=False,
#     task_ack_late=False,
# )

# change configurations(method 2)
app.config_from_object("CeleryConf")


@app.task(name="SimpleTask.add", task_time_limit=5)
def add(a, b):
    time.sleep(10)
    return a + b


@app.task(name="SimpleTask.div", bind=True, default_retry_delay=100)
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


@app.task
def show(name):
    print(f"Your name is {name}")


@signals.task_prerun.connect
def print_hello(sender=None, **kwargs):
    print("hello.")


@signals.task_postrun.connect
def print_goodbye(sender=None, **kwargs):
    print("good bye.")


@signals.task_success.connect(sender=add)
def add_success(sender=None, **kwargs):
    print("add did.")


@signals.task_success.connect(sender=div)
def div_success(sender=None, **kwargs):
    print("div did.")


@signals.worker_shutdown.connect
def goodbye_worker(sender=None, **kwargs):
    print("Worker: Goodbye dude.")


@signals.worker_ready.connect
def hi_worker(sender=None, **kwargs):
    print("Worker: Hi dude.")
