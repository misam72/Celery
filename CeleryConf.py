from celery.schedules import crontab
from kombu import Queue, Exchange

task_time_limit = 60
task_soft_time_limit = 50
worker_concurrency = 3
worker_perfetch_multiplier = 1
task_ignore_result = False
task_always_eager = False
task_ack_late = False

beat_schedule = {
    "call-show-every-one-minute": {
        "task": "SimpleTask.show",
        "schedule": crontab(minute="*/1"),
        "args": ("misam",),
    }
}

default_exchange = Exchange("default", type="direct")
media_exchange = Exchange("media", type="fanout")

task_queues = (
    Queue("default", default_exchange, routing_key="default"),
    Queue("video", media_exchange, routing_key="video"),
    Queue("image", media_exchange, routing_key="image"),
)

task_default_queue = "default"
task_default_exchange = "default"
task_default_routing_key = "default"

task_routes = {"SimpleTask.add": {"queue": "video"}, "SimpleTask.div": {"queue":"image"}}
