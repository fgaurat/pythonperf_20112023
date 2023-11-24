import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
import threading
from  concurrent.futures import ThreadPoolExecutor


def download(url_log):
    response = requests.get(url_log)
    file_name = url_log.split('/')[-1]
    with open(file_name,'w') as f:
        f.write(response.text)

def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    all_logs = [url+a["href"] for a in all_a if ".log" in a["href"]]
    
    all_threads = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download,all_logs)

    # for url_log in all_logs:
    #     th = threading.Thread(target=download,args=[url_log])
    #     th.start()
    #     all_threads.append(th)
    
    # for th in all_threads:
    #     th.join()
        
    end = time.perf_counter()
    print(end-start)
    # 0.5712224000017159
    # 0.18424520001281053 th


if __name__=='__main__':
    main()
