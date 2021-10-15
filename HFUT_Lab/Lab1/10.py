import random
def foo(n):
    list=[random.randint(1,1000) for i in range(n)]
    aver=sum(list)/len(list)
    L=[aver]
    for item in list:
        if item>aver:
            L.append(item)
    tuple(L)
    print(L)

foo(int(input("Please input an integer: ")))