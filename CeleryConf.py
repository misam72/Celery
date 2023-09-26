from celery.schedules import crontab

task_time_limit = 60
task_soft_time_limit = 50
worker_concurrency = 3
worker_perfetch_multiplier = 1
task_ignore_result = False
task_always_eager = False
task_ack_late = False

beat_schedule={
    "call-show-every-one-minute":{
        "task": "SimpleTask.show",
        "schedule":crontab(minute="*/1"),
        "args": ("misam",),
    }
}
