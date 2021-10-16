import string
num=input("Please input an integer: ")
ll=[]
for item in num:
    ll.append(item)
ll.reverse()
print(len(ll))
for x in ll:
    print(x,end=' ')