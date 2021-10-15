# slice
import random
list=[random.randint(0,100) for i in range(20)]
print(list)
y=list[::2]
y.sort(reverse=True)
list[::2]=y
print(list)