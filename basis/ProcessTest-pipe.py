
"""
管道
"""

from multiprocessing import Process,Pipe

class Consumer(Process):
    def __init__(self,pipe):
        Process.__init__(self)
        self.pipe=pipe

    def run(self):
        self.pipe.send('Consumer Words')
        print('Consumer Received:', self.pipe.recv())

class Producer(Process):
    def __init__(self,pipe):
        Process.__init__(self)
        self.pipe=pipe

    def run(self):
        self.pipe.send('Producer Received')
        print('Producer Words:', self.pipe.recv())

if __name__ == '__main__':
    pipe = Pipe()
    p=Producer(pipe[0])
    c=Consumer(pipe[1])
    p.daemon=c.daemon=True
    p.start()
    c.start()
    p.join()
    c.join()
    print('end')


    
    