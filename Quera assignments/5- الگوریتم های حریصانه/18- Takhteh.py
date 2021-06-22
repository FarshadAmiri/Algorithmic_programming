n, c = map(int, input().split())
x = list(map(int, input().split()))

x.sort(reverse = True)

if max(x) >= 2*c:
    print(0)
elif max(x) <= c:
    print(c)
elif (max(x) >c) and (max(x) < 2*c):
    for xi in x:
        c = c - max(0,(xi - c))
        if c <= 0:
            c = 0
            break
    print(c)