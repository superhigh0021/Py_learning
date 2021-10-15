import random
chance=2
x=random.randint(0,100)
while chance>=0:
    input=int(input("Please input an integer(from 0 to 100): "))
    if input==x:
        print("Right!")
        break
    elif input<x:
        print("Too small!")
    else:
        print("Too large")
    del input
    chance=chance-1
    if chance==0:
        print("Game over,the right answer is %d"%x)