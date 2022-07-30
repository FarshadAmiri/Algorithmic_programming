from itertools import permutations

n = int(input())
a = int(input().replace(' ',''))
# n, a = 3, 312
print(a)

perms = list(map(int, [''.join(p) for p in permutations(str(a))]))
print(perms)

