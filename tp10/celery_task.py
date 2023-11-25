from celery import Celery, signature, group

import httpx

app = Celery('app_hello', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")

@app.task
def bonjour(name):
    return f'hello world {name}'

@app.task
def bonjour_2(name):
    return {"name":name,"message":f'hello world {name}'}


@app.task
def download(url):
    response = httpx.get(url)
    d = {
        "data":response.text,
        "file_name":url.split('/')[-1]
    }
    return d
    

@app.task        
def save(d):
    print(d)
    file_content = d['data']
    file_name= d['file_name']
    with open(file_name,'w') as f:
        f.write(file_content)
