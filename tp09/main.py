import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint

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
    
    for url_log in all_logs:
        download(url_log)
        
    end = time.perf_counter()
    print(end-start)


if __name__=='__main__':
    main()
