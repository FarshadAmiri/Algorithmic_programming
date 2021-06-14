n = int(input())
array = list(map(int, input().split(' ')))   # or => array = [int(item) for item in input().split()]

for i in range(1,n):
    p = i
    while (p>0) and (array[p] > array[p-1]):
        array[p], array[p-1] = array[p-1] , array[p]
        p = p-1

for i in list(reversed(array)):
    print(i, end=' ')