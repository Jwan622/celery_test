from celery_test.tasks import add, multiply, subtract

result_add = add.delay(4, 2)
print(f"Add Result: {result_add.get()}")

result_multiply = multiply.delay(5)
print(f"Multiply Result: {result_multiply.get()}")

result_subtract = subtract.delay(3)
print(f"Subtract Result: {result_subtract.get()}")
