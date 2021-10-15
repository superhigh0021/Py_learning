def solve():
    m=365//7
    n=365%7
    workday=m*5+n
    weekend=m*2
    a=37.78
    a=a-17.78-0.1*weekend-1
    return float(a/workday)

print(solve())