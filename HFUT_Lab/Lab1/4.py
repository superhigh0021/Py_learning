for item in range(1,1001):
    L=[]
    for i in range(1,item):
        if item % i==0:
            L.append(i)
    sum=sum(L)
    if sum==item:
        print('%d '%sum,end='')
    del L
    del sum
print('\n')