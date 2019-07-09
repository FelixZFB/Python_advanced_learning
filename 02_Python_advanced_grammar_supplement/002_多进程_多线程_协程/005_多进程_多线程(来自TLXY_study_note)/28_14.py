
import multiprocessing
import os
from time import sleep, ctime

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    print("module name: ", __name__)
    print("parent process: ", os.getppid())
    print("process id: ", os.getpid())







