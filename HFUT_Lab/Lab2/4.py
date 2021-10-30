from random import randint
class Myqueue:
    def __init__(self):
        self.data=[]
        self.size=100
        self.current=0
    def is_empty(self):
        if self.current==0:
            return True
        else:
            return False
    def is_full(self):
        if self.current < self.size:
            return False
        else:
            return True
    def get_head(self):
        if self.is_empty():
            print('The deque is empty now, please retry!')
        else:
            return self.data[0]
    def enqueue(self,elem):
        if self.is_full():
            print("The deuqe is full now, please retry!")
        else:
            self.data.append(elem)
            self.current+=1
    def dequeue(self):
        if self.is_empty():
            print("The deque is empty now, please retry!")
        else:
            for i in range(len(self.data)-1):
                self.data[i]=self.data[i+1]
            self.current-=1
            del self.data[-1]
    def print(self):
        print(self.data)

queue=Myqueue()
print(queue.is_empty())
n=int(input("Please input the ideal size of your deque: "))
for _ in range(n):
    queue.enqueue(randint(0,100))
print(queue.is_empty())
queue.print()
print()
queue.dequeue()
queue.print()
print(queue.get_head())