import random
list=[random.randint(0,100) for i in range(50)]
print(list)
for index in range(len(list)-1,-1,-1):
    if list[index]%2!=0:
        del list[index]
print(list)