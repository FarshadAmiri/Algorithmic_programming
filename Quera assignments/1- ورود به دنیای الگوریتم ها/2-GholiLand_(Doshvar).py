import bisect

n , q = map(int, input().split())
c = list(map(int, input().split()))

days = [int(input()) for i in range(q)]

def merge_sort(arr, l, r):
    if r - l == 1:
        return

    mid = int((l + r) / 2)

    merge_sort(arr, l, mid)
    merge_sort(arr, mid, r)

    p1, p2 = l, mid
    b = []

    while (p1 < mid) or (p2 < r):
        if p1 == mid:
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


merge_sort(c, 0, len(c))


for day in days:
    print(bisect.bisect_right(c, day-0.1))

