from SimpleTask import add, div


add.apply_async((52,52), countdown=1)
div.delay(1,0)