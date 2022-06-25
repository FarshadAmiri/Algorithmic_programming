import random, time
import heapq

def manually_remove_minimum(list):
    min_number = min(list)
    list.remove(min_number)
    return list


# ppl = [11,5,4,19,12,3,4,15,14,17]
# ppl2 = [11,5,4,19,12,3,4,15,14,17]

ppl = [random.randint(0,5000) for i in range(1000000)]
# print(ppl)

t2 = time.time()
manually_remove_minimum(ppl)
print(f'{(time.time() - t2):.5f} seconds [Manual computation]')

t1 = time.time()
heapq.heapify(ppl)
heapq.heappop(ppl)
# print(ppl, type(ppl))
print(f'{(time.time() - t1):.5f} seconds [Heaped computation]')


