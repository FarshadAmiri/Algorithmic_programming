from sys import setrecursionlimit

setrecursionlimit(1000000000)
def power(a, b):
    if b == 0:
        return 1
    res = power(a, b//2)

    res = res * res
    if b % 2 == 1:
        res *=a


    return res

base, exp = float(input()) , float(input())
res = 1
print(f'{power(base, exp):.3f}')