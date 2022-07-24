import math
n , q = map(int, input().split())
series = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(q)]

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


def calculate_arbitrary_max(l,r):
    global ranges, max_in_ranges, series
    if l == r:
        return series[l]
    sub_ranges = []
    sub_ranges_maxes = []
    for idx, rr in enumerate(ranges):
        if (rr[0] >= l) and (rr[1] <= r):
            sub_ranges_maxes.append(max_in_ranges[idx])
            sub_ranges.append((rr[0], rr[1]))
    if len(sub_ranges_maxes) > 0:
        start_range = min([i[0] for i in sub_ranges])
        end_range = max([i[1] for i in sub_ranges])
        outer_left = [i for i in range(l, start_range)]
        outer_right = [i for i in range(end_range + 1, r + 1)]
        for i in outer_left:
            sub_ranges_maxes.append(series[i])
        for i in outer_right:
            sub_ranges_maxes.append(series[i])
    else:
        for i in range(l, r + 1):
            sub_ranges_maxes.append(series[i])
    return max(sub_ranges_maxes)


for query_type, i,j in queries:
    if query_type == 1:
        print(calculate_arbitrary_max(i,j))
    elif query_type == 2:
        series[i] = j
        for l,r in ranges:
            if (i >= l) and (i <= r):
                calculate_max_in_range(l, r)
                break