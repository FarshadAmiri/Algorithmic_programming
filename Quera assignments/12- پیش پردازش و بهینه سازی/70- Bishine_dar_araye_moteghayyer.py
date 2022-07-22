n , q = map(int, input().split())
series = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(q)]


for query_type, i,j in queries:
    if query_type == 1:
        print(max(series[i:j+1]))
    if query_type == 2:
        series[i] = j