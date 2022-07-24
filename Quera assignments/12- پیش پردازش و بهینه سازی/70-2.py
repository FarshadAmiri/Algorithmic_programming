# n , q = map(int, input().split())
# series = list(map(int, input().split()))
# queries = [list(map(int, input().split())) for i in range(q)]
n, q, series, queries = 14, 10, [7,0,5,4,3,6,9,7,4,-4,2,2,9,1], [[1, 0, 11], [2, 0, 8], [1, 4, 6], [1, 7, 10], [2, 3, 7], [1, 0, 3], [1,4,8], [2,5,17], [2,11,7], [1,6,11]]

def change_val(idx, new_val):
    global series
    series[idx] = new_val


for query_type, i,j in queries:
    if query_type == 1:
        print(max(series[i:j+1]))
    if query_type == 2:
        change_val(i, j)