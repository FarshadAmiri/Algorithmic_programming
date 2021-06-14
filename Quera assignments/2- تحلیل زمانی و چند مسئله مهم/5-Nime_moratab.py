n = int(input())
serie = list(map(int, input().split(' ')))

faults = 0
for i in range(n):
    if serie[i] != i+1:
        faults += 1
    if faults>2:
        break

if faults==2:
    print('YES')
else:
    print('NO')