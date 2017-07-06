import os
import time
import threading
import multiprocessing
from Download import request
from MongoQueue import MongoQueue
from bs4 import BeautifulSoup

SLEEP_TIME = 1

def mzitu_crawler(max_threads=10):
    crawl_queue = MongoQueue('meinvxiezhenji','crawl_queue')
    
    def pageurl_crawler():
        while True:
            try:
                url = crawl_queue.pop()
                print('开始请求 - > ',url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                img_urls = []
                req = request.get(url,3).text
                title = crawl_queue.pop_title(url)
                mkdir(title)
                os.chdir('/Users/pp/Demo/python-study/Crawler/mzitu'+title)
                max_span = BeautifulSoup(req, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()

                for page in range(1,int(max_span)+1):
                    page_url = url + '/' + str(page)
                    img_url = BeautifulSoup(request.get(page_url, 3).text, 'lxml').find('div', class_='main-image').find('img')['src']
                    img_urls.append(img_url)
                    save(img_url)
                crawl_queue.complete(url)

    def save(img_url):
        name = img_url[-9:-4]
        img = request.get(img_url,3)
        print(u'写入文件 ->  ',name)
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    def mkdir(path):
        path = path.strip()
        isExists = os.path.exists(os.path.join('mzitu',path))
        if not isExists:
            print(u'创建了文件夹 ->  ',path)
            os.makedirs(os.path.join('/Users/pp/Demo/python-study/Crawler/mzitu',path))
            os.chdir(os.path.join('/Users/pp/Demo/python-study/Crawler/mzitu',path))
            return True
        else:
            print(path,u'文件夹已存在')
            return False

    threads = []
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive(): ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        while len(threads) < max_threads or crawl_queue.peek(): ##线程池中的线程少于max_threads 或者 crawl_qeue时
            thread = threading.Thread(target=pageurl_crawler) ##创建线程
            thread.setDaemon(True) ##设置守护线程
            thread.start() ##启动线程
            threads.append(thread) ##添加进线程队列
        time.sleep(SLEEP_TIME)

def process_crawler():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print('将会启动进程数为：', num_cpus)
    for i in range(num_cpus):
        p = multiprocessing.Process(target=mzitu_crawler) ##创建进程
        p.start() ##启动进程
        process.append(p) ##添加进进程队列
    for p in process:
        p.join() ##等待进程队列里面的进程结束
 
if __name__ == "__main__":
    process_crawler()
