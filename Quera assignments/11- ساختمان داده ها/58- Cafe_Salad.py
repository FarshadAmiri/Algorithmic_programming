q = int(input())
ops = []

for i in range(q):
    l = input().split()
    n = 1
    day_ops = []
    while n <= int(l[0]):
        day_ops.append((l[2 * n - 1], int(l[2 * n])))
        n += 1
    ops.append(day_ops)

print(ops)