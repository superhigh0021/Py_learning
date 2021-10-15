from math import sqrt
list=[2]
x=int(input("Please input an integer(x>2): "))
for item in range(3,x):
    for i in range(2,int(sqrt(item))):
        if item%i==0:
            break;
    else:
        list.append(item)
print(list)