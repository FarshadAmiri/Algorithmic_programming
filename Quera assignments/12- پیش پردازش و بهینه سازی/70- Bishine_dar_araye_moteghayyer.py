import math
# n , q = map(int, input().split())
# series = list(map(int, input().split()))
# queries = [list(map(int, input().split())) for i in range(q)]
n, q, series, queries = 5, 6, [1, 2, 3, 4, 5], [[1, 1, 3], [2, 1, 5], [1, 1, 3], [1, 0, 4], [2, 3, 7], [1, 0, 3]]

r = math.floor(math.sqrt(n))
nr = math.ceil(math.sqrt(n))
ranges = []
max_in_ranges = [None] * nr

for i in range(nr):
    if i + 1 == nr:
        ranges.append((i * r, n-1))
    else:
        ranges.append((i * r, (i + 1) * r - 1))


def calculate_max_in_range(l,r):
    global ranges, max_in_ranges
    for index,rr in enumerate(ranges):
        if rr[0] == l:
            max_in_ranges[index] = max(series[l:r+1])
            break

for i,j in ranges:
    calculate_max_in_range(i,j)

# print(f' series = {series} \n ranges = {ranges} \n max_in_ranges = {max_in_ranges}')

def calculate_arbitrary_max(l,r):
    global ranges, max_in_ranges, series
    sub_ranges_maxes = []
    for idx,rr in enumerate(ranges):
        if (rr[0] >= l) and (rr[1] <= r):
            sub_ranges_maxes.append(max_in_ranges[idx])
        elif (rr[0] < l) and (rr[1] >= l):
            for x in range(l, rr[1] + 1):
                sub_ranges_maxes.append(series[x])
        elif (rr[0] <= r) and (rr[1] > r):
            for x in range(rr[0], r + 1):
                sub_ranges_maxes.append(series[x])
    return max(sub_ranges_maxes)



for query_type, i,j in queries:
    if query_type == 1:
        print(calculate_arbitrary_max(i,j))
    elif query_type == 2:
        series[i] = j
        for l,r in ranges:
            if (i >= l) and (i <= r):
                rr = (l,r)
                break
        calculate_max_in_range(rr[0],rr[1])