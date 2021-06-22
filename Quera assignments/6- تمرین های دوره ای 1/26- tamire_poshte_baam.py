n = int(input())
roofs = list(map(int, input().split()))

min_roofs = []

for i in range(n,-1,-1):
    if i == n - 1:
        min_roofs.append(i)
    if i < n - 1:
            if roofs[i] < roofs[min_roofs[-1]]:
                min_roofs.append(i)
min_roofs.reverse()
# print(min_roofs)

min_roofs_unique = list(dict.fromkeys(min_roofs))
# print(min_roofs_unique)

loc = 0
cost = 0
for i in min_roofs_unique:
    cost += (i + 1 - loc) * roofs[i]
    loc = i + 1

print(cost)




