from multiprocessing import Process
import os

def example():
    print('children_fork id={}'.format(os.getpid()))

p=Process(target=example)
print('father_fork id={}'.format(os.getpid()))
p.start()
p.join()