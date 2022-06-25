import heapq, math, random
# numbers = [int(input()) for i in range(int(input()))]
# numbers = [3,9,1,4,12,15,8,7,12,11,1,6,11,8,4]
numbers = [random.randint(0,100) for i in range(20)]
print(numbers)

h1 = [numbers[0]]
h2 = []
print(h1[0])

if numbers[1] >= h1[0]:
    h2.append(numbers[1])
else:
    h1 = [numbers[1]]
    h2 = [numbers[0]]

print(h1[0], h1[0] == h1[0])

for id,x in enumerate(numbers[2:]):
    heapq._heapify_max(h1)
    heapq.heapify(h2)

    if x > h1[0]:
        heapq.heappush(h2, x)
        if len(h2) > len(h1):
            h1.append(heapq.heappop(h2))
    else:
        heapq.heappush(h1, x)
        if len(h1) > len(h2) + 1:
            heapq.heappush(h2, heapq._heappop_max(h1))

    heapq._heapify_max(h1)

    real_median = sorted(numbers[:id+3])[math.ceil(((id+3)/2)-1)]
    print(f'{x} Added --> {h1[0]}  real_median = {real_median} {real_median == h1[0]}')

