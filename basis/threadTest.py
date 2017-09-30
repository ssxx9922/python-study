# coding:utf-8

import threading
import _thread
import time

# def print_time(thredName,delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print(thredName,time.ctime())

# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#     print('error : 无法启动线程')

# while 1:
#     pass


exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程：' + self.name)
        print_time(self.name, self.counter, 5)
        print('结束线程：' + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, 'thread-1', 1)
thread2 = myThread(2, 'thread-2', 2)

thread1.start()
thread2.start()
thread1.join()  # 等待线程结束，在继续主线程
thread2.join()

print('退出主线程')
