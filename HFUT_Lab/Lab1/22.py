from random import randint

llist=[randint(0,100) for _ in range(randint(50,100))]
print(llist)
dic=dict()
for item in llist:
    if dic.get(item,0)==0:
        dic[item]=1
    else:
        dic[item]+=1
print(dic)