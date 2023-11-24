from celery import Celery

app = Celery('app_hello', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")
@app.task
def bonjour():
    return 'hello world'