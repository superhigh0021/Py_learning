str=input('Please input a string of binary: ')
list=str.split(',')
llist=[]
for item in list:
    num=int(item,2)
    if num%5==0:
        llist.append(item)
print(','.join(llist))