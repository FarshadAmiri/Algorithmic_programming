n = int(input())
Set = list(map(int, input().split(' ')))

d = dict()
for mask in range(2**n):
    l = []
    for i in range(n):
        if mask & (2**i):
            l.append(Set[i])
    d[mask+1] = l

result = 1e10
for key,value in d.items():
    diff = abs(sum(value) - sum(d[(2**n)+1-key]))
    if diff < result:
        result = diff

print(result)