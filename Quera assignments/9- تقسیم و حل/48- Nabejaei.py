n = int(input())
series = list(map(int, input().split()))


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


def inversion(a, l, r):
    if r - l <= 1:
        return 0

    mid = int((l+r)/2)
    result = 0

    result = result + inversion(a, l ,mid)
    result = result + inversion(a, mid, r)

    k = 0

    for i in range(l, mid):
        while (k < (r - mid)) and (a[i] > a[k + mid]):
            k += 1
        result += k

    merge_sort(a, l, r)
    return result


print(inversion(series, 0, len(series)))