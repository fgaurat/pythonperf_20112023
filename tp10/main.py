from celery import Celery,signature,group,chain
from pprint import pprint
from bs4 import BeautifulSoup
import httpx


app = Celery('hello', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")



def main():
    # hello = app.send_task("celery_task.bonjour")
    # result = hello.get()
    # print(result)
    url="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    all_logs = [url+a["href"] for a in all_a if ".log" in a["href"]]
    # pprint(all_logs)

    # f = signature('celery_task.bonjour')
    # r = f.delay()
    # result = r.get()
    # print(result)
    # f = signature('celery_task.bonjour_2')
    # r = f.delay("fred")
    # result = r.get()
    # print(result)


    # f = signature('celery_task.download')
    # r = f.delay(all_logs[0])
    # result = r.get()


    # Tous les téléchargements
    # g = group(signature('celery_task.download', args=[url]) for url in all_logs)()
    # results = g.get()
    # toutes les sauvegardes
    # g = group(signature('celery_task.save', args=[result]) for result in results)()
    
    # chainage d'un téléchargement et d'une sauvegarde, le sortie du premier (download )est l'entrée du second (save)
    # download(url) | save
    
    res = chain(signature('celery_task.download',args=[all_logs[0]]), signature('celery_task.save'))()

    r = res.get()
    print(r)
        
    
if __name__=='__main__':
    main()

