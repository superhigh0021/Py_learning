import random
import string


def getlen(elem):
    return len(elem)


def create_list(n, m):
    x = string.ascii_letters + string.digits
    ll = [
        ''.join([random.choice(x) for _ in range(random.randint(1, m + 1))])
        for _ in range(n)
    ]
    #print(ll)
    ll.sort(key=getlen, reverse=True)
    print(ll)


create_list(5, 6)
