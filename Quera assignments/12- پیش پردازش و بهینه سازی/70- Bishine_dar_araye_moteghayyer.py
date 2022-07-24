import math
n , q = map(int, input().split())
series = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(q)]
# n, q, series, queries = 5, 6, [1, 2, 3, 4, 5], [[1, 1, 3], [2, 1, 5], [1, 1, 3], [1, 0, 4], [2, 3, 7], [1, 0, 3]]
# n, q, series, queries = 26, 4, [7,0,5,4,3,6,9,7,4,4,2,2,9,1,7,6,8,4,0,12,5,6,9,3,8,5], [[1, 7, 7.], [2, 1, 8], [1, 0, 0], [1, 7, 10], [2, 3, 7], [1, 0, 3], [1,4,8], [2,5,17], [2,11,7], [1,6,11]]

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
