from SimpleTask import add, div, show

# running flower:
# celery --broker=amqp://guest:guest@0.0.0.0:5672// flower

result1 = add.apply_async((52,52), countdown=1)
result2 = div.delay(1,1)