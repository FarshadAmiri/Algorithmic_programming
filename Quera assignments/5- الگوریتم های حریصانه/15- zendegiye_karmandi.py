n = int(input())
tasks = list(map(int, input().split(' ')))

tasks.sort()

j = 0
for i in range(len(tasks)):
    if j < tasks[i]:
        j += 1
print(j)