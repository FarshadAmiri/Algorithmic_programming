n, en = map(int, input().split())
fruits = []
for i in range(n):
    t, g = map(int, input().split())
    fruits.append((t, g))

fruits.sort(key= lambda x: x[0])

for fruit in fruits:
    if fruit[0] <= en:
        if fruit[1] > fruit[0]:
            en += fruit[1] - fruit[0]
print(en)

