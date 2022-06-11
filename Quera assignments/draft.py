import heapq

myHeap = [3, 1, 5]

heapq.heapify(myHeap) # make a heap with elements of (myHeap = [3, 1, 5]) and store it in myHeap
heapq.heappush(myHeap, -5) # add -5 to myHeap
print(myHeap)
print(type(myHeap))
minElement =  heapq.heappop(myHeap)  # pop min element in myHeap and return value of min element

print(minElement) # print -5