candies = list(map(int, input().split()))
a, c = candies[0], candies[2]

guys = {1: 0, 2: 0, 3: 0, 4: 0}

i = 1
while (a > 0) and (c > 0):
    if i == 5:
        i = 1
    guys[i] += 1
    a -= 1
    i += 1
    if (a == 0):
        break
    if i == 5:
        i = 1
    guys[i] += 1
    c -= 1
    i += 1

for i in range(1,5):
    print(guys[i], end=' ')