from random import randint


def create_tuple(n, m):
    g = (randint(0, m) for _ in range(n))
    ttuple = tuple(g)
    for item in ttuple:
        if item % 2 != 0:
            print(item, end=' ')
    print()


create_tuple(20, 100)
