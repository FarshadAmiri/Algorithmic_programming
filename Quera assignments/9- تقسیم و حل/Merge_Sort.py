# arr = list(map(int, input().split()))
arr = [41,15,37,52,14,65,26,12]

def merge_sort(arr, l, r):
    if r - l == 1:
        return

    mid = int((l + r) / 2)

    merge_sort(arr, l, mid)
    merge_sort(arr, mid, r)

    p1, p2 = l, mid
    b = []

    while (p1 < mid) or (p2 < r):
        if (p1 == mid+1) and (p2 == r+1):
            return b
        elif p1 == mid:
            b.append(arr[p2])
            p2 += 1
        elif p2 == r:
            b.append(arr[p1])
            p1 += 1
        elif arr[p1] <= arr[p2]:
            b.append(arr[p1])
            p1 += 1
        else:
            b.append(arr[p2])
            p2 += 1
    arr[l:r] = b


merge_sort(arr, 0, len(arr))
print(arr)