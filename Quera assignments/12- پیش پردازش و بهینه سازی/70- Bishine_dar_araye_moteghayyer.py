import math
# n , q = map(int, input().split())
# series = list(map(int, input().split()))
# queries = [list(map(int, input().split())) for i in range(q)]
n, q, series, queries = 5, 6, [1, 2, 3, 4, 5], [[1, 1, 3], [2, 1, 5], [1, 1, 3], [1, 0, 4], [2, 3, 7], [1, 0, 3]]

r = math.floor(math.sqrt(n))
nr = math.ceil(math.sqrt(n))
ranges = []
max_in_ranges = [None for i in range(nr)]

for i in range(nr):
    if i + 1 == nr:
        ranges.append((i * r, n-1))
    else:
        ranges.append((i * r, (i + 1) * r - 1))


def calculate_max_in_range(l,r):
    global ranges, max_in_ranges
    for index,rr in enumerate(ranges):
        if rr[0] == l:
            idx = index
            break
    max_in_ranges[idx] = max(series[l:r+1])

for i,j in ranges:
    calculate_max_in_range(i,j)

# print(series, ranges, max_in_ranges, sep='\n')

def calculate_arbitrary_max(l,r):
    global ranges, max_in_ranges, series
    sub_ranges_idx = []
    out_data = []
    for idx,rr in enumerate(ranges):
        if (rr[0] >= l) and (rr[1] <= r):
            sub_ranges_idx.append(idx)
        elif (rr[0] < l) and (rr[1] >= l):
            for x in range(l, rr[1] + 1):
                out_data.append(series[x])
        elif (rr[0] <= r) and (rr[1] > r):
            for x in range(rr[0], r + 1):
                out_data.append(series[x])
    # print('out_data = ',out_data)
    # print('sub_ranges_idx = ', sub_ranges_idx)
    # print('max_in_ranges', max_in_ranges)
    maxes = []
    for ii in sub_ranges_idx:
        maxes.append(max_in_ranges[ii])

    return max(max(maxes), max(out_data))

print(calculate_arbitrary_max(0,2))


