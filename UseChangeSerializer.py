from ChangeSerializer import call
from Person import Persons

p = Persons('jax', 35)
result = call.delay(p)
print(result.get())