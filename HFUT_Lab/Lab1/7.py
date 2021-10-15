def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

def judge(n):
    x=1
    while x>0:
        if fib(x)<n:
            print('%d '%fib(x),end='')
            x+=1
        else:
            break;
x=int(input("Please input an integer: "))
judge(x)
print()