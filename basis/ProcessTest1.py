#coding:utf-8
"""
进程锁
"""

from multiprocessing import Process,Lock
import time

class MyProcess(Process):
    def __init__(self,loop):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            self.lock.acquire()
            print('pid:',str(self.pid),'loopCount:',str(count))
            self.lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10,15):
        p = MyProcess(i)
        # p.daemon = True
        p.start()
        # p.join()

    print('main process end!')