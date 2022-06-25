import heapq
numbers = [int(input()) for i in range(int(input()))]

# print(numbers)

h1 = [numbers[0]]
h2 = []

if numbers[1] >= h1[0]:
    h2.append(numbers[1])
else:
    h1 = [numbers[1]]
    h2 = [numbers[0]]


for i in numbers[1:]:
    heapq.heapify(h1)
    heapq.heapify(h2)
    heapq._heapify_max(h1)



