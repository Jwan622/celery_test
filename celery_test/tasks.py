from celery_app import app
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


@app.task
def add(x, y):
    result = x + y
    r.set('add_result', result)
    print(f"Task add: {result}")
    return result


@app.task
def multiply(x):
    add_result = int(r.get('add_result'))
    result = add_result * x
    r.set('multiply_result', result)
    print(f"Task multiply: {result}")
    return result


@app.task
def subtract(x):
    multiply_result = int(r.get('multiply_result'))
    result = multiply_result - x
    print(f"Task subtractttt: {result}")
    return result
