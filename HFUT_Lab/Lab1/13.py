import random
import string
x = string.ascii_letters + string.digits + string.punctuation
list = [random.choice(x) for _ in range(1000)]
str = ''.join(list)
dict={}

for item in list:
    dict[item]=dict.get(item,0)+1
print(dict)

llist=[x for x in input('Please enter a string:').split(',')]
llist.sort()
print(','.join(llist))