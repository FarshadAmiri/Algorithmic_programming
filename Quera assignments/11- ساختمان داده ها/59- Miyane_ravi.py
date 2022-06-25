import heapq

numbers = [int(input()) for i in range(int(input()))]

h1 = [-numbers[0]]
h2 = []
print(-h1[0])

if numbers[1] >= -h1[0]:
    h2.append(numbers[1])
else:
    h1 = [-numbers[1]]
    h2 = [numbers[0]]

print(-h1[0])

for x in numbers[2:]:
    heapq.heappush(h1, -x)
    if (len(h1) > len(h2) + 1) or (-h1[0] > h2[0]):
        heapq.heappush(h2, -heapq.heappop(h1))

    if len(h2) > len(h1):
        heapq.heappush(h1, -heapq.heappop(h2))

    print(-h1[0])