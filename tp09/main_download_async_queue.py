import asyncio
import time
from bs4 import BeautifulSoup
from pprint import pprint
import httpx

async def olddownload(url_log):
    async with httpx.AsyncClient() as client:
        response = await client.get(url_log)
        file_name = url_log.split('/')[-1]
        with open(file_name,'w') as f:
            f.write(response.text)

async def download(download_queue,save_queue):
    while True:
        url = await download_queue.get()
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            d = {
                "data":response.text,
                "file_name":url.split('/')[-1]
            }
            save_queue.put_nowait(d)
        download_queue.task_done()
        
async def save(save_queue):
    while True:
        d = await save_queue.get()
        data = d['data']
        file_name= d['file_name']
        with open(file_name,'w') as f:
            f.write(data)
        save_queue.task_done()

async def main():
    start = time.perf_counter()
    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 3
    
    url="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    all_logs = [url+a["href"] for a in all_a if ".log" in a["href"]]
    tasks = []
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(download_queue,save_queue))
        tasks.append(task)

    for i in range(nb_save_workers):
        task = asyncio.create_task(save(save_queue))
        tasks.append(task)
        

    
    for url in all_logs:
        download_queue.put_nowait(url)
        
    await download_queue.join()
    await save_queue.join()

    for t in tasks:
        t.cancel()
        
    end = time.perf_counter()
    print(end-start)
    # 0.5712224000017159
    # 0.29707670002244413
    # 0.31163179999566637 5 wks
    # 0.36933650000719354 10 wks
    
    

if __name__=='__main__':
    asyncio.run(main())
