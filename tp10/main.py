from celery import Celery
app = Celery('hello', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")



def main():
    hello = app.send_task("celery_task.bonjour")
    result = hello.get()
    print(result)
if __name__=='__main__':
    main()

