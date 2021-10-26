from random import randint

list=[randint(0,100) for _ in range(1,randint(0,20))]
print(list)
print(list[::])
print(list[::-1])
print(list[::2])
