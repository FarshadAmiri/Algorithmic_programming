n, k = map(int, input().split())
arr = []

for row in range(k):
    arr.append(list(map(int, input().split())))

# print(arr)

def merge(a,b):
    p1, p2 = 0, 0
    merged = []
    while (p1 <= len(a)) or (p2 <= len(b)):
        if (p1 == len(a)) and (p2 == len(b)):
            return merged
        elif p1 == len(a):
            merged.append(b[p2])
            p2 += 1
        elif p2 == len(b):
            merged.append(a[p1])
            p1 += 1
        elif a[p1] >= b[p2]:
            merged.append(b[p2])
            p2 += 1
        elif a[p1] < b[p2]:
            merged.append(a[p1])
            p1 += 1

# print(merge([1,4,100],[4,4,8]))

def merge_sort(arrays):
    if len(arrays) == 1:
        return arrays[0]
    elif len(arrays) == 2:
        return merge(arrays[0], arrays[1])
    elif len(arrays) >= 3:
        mid = len(arrays)//2
        return merge(merge_sort(arrays[:mid]), merge_sort(arrays[mid:]))

print(*merge_sort(arr))