import random
x=random.randint(0,100)
input=int(input("Please enter an integer(from 0 to 100): "))
if input==x:
    print("Right!")
elif input<x:
    print("Too small, the right answer is %d"%x)
else:
    print("Too large, the right answer is %d"%x)    