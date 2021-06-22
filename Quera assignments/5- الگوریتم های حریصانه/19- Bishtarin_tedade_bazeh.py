n = int(input())
x = list(map(int, input().split()))
nums = []
for i in range(0, len(x) - 1, 2):
    nums.append((x[i], x[i + 1]))

nums.sort(key=lambda x: x[1])

last_r = -1
ans = 0
for i in nums:
    if last_r <= i[0]:
        last_r = i[1]
        ans += 1

print(ans)
