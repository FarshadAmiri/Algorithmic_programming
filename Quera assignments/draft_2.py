import heapq

h = [8,4,6,9,11,4,3,15,2]

heapq.heapify(h)
print(h)
print(h[0])
print(heapq.heappop(h))

heapq._heapify_max(h)
print(h)
print(h[0])
print(heapq._heappop_max(h))