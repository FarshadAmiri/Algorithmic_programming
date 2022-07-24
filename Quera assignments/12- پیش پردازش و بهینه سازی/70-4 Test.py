import random
import math
# Generating inputs
n, q = 100, 20

def generating_input(n,q):
    series = [random.randint(0,n-1) for i in range(n)]
    q1_1 = [random.randint(0,n-2) for i in range(q)]
    q1_2 = [random.randint(x, n - 2) for x in q1_1]
    q1 = [[1, q1_1[i], q1_2[i]] for i in range(q)]
    q2 = [[2, random.randint(0,n-1), random.randint(0,n-1)] for i in range(q)]
    select = [random.randint(0,3) for i in range(q)]
    queries = [q2[i] if (select[i] == 0) else q1[i] for i in range(q)]
    return series, queries

# series, queries = generating_input(n,q)
series =  [74, 96, 22, 81, 21, 16, 64, 38, 77, 8, 43, 36, 71, 44, 56, 78, 30, 43, 65, 58, 88, 75, 48, 2, 81, 57, 79, 63, 25, 4, 19, 42, 8, 35, 52, 93, 15, 43, 73, 25, 74, 87, 40, 13, 77, 17, 13, 50, 55, 20, 83, 6, 34, 4, 46, 21, 91, 81, 71, 11, 83, 75, 96, 22, 38, 22, 97, 97, 6, 70, 74, 57, 9, 29, 64, 15, 76, 42, 51, 20, 80, 41, 33, 12, 12, 66, 36, 31, 59, 3, 32, 40, 27, 13, 29, 2, 11, 64, 87, 52]
queries =  [[1, 95, 97], [2, 99, 60], [1, 95, 96], [1, 95, 98], [1, 7, 90], [1, 12, 88], [1, 66, 82], [1, 93, 98], [2, 52, 20], [1, 16, 19], [1, 18, 79], [1, 62, 64], [1, 79, 81], [1, 37, 81], [1, 4, 67], [2, 18, 98], [1, 83, 87], [1, 13, 82], [1, 50, 76], [2, 40, 57]]
print('series = ',series,'\nqueries = ', queries)

def MySolution(n, q, series, queries):
    answer = []
    r = math.floor(math.sqrt(n))
    nr = math.ceil(math.sqrt(n))
    ranges = []
    max_in_ranges = [None] * nr

    for i in range(nr):
        if i + 1 == nr:
            ranges.append((i * r, n - 1))
        else:
            ranges.append((i * r, (i + 1) * r - 1))

    def calculate_max_in_range(l, r):
        for index, rr in enumerate(ranges):
            if rr[0] == l:
                max_in_ranges[index] = max(series[l:r + 1])
                break

    for i, j in ranges:
        calculate_max_in_range(i, j)

    # print(f' series = {series} \n ranges = {ranges} \n max_in_ranges = {max_in_ranges}')

    def calculate_arbitrary_max(l, r):
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

    for query_type, i, j in queries:
        if query_type == 1:
            answer.append(calculate_arbitrary_max(i, j))
        elif query_type == 2:
            series[i] = j
            for l, r in ranges:
                if (i >= l) and (i <= r):
                    calculate_max_in_range(l, r)
                    break
    return answer

def CostlySolution(n,q,series, queries):
    answer = []
    for query_type, i, j in queries:
        if query_type == 1:
            answer.append(max(series[i:j + 1]))
        if query_type == 2:
            series[i] = j
    return answer

ans_my = MySolution(n, q, series, queries)
ans_costly =  CostlySolution(n,q,series, queries)

print(f'ans_my =     {ans_my}', f'ans_costly = {ans_costly}', sep='\n')
print(True if ans_my == ans_costly else False)
