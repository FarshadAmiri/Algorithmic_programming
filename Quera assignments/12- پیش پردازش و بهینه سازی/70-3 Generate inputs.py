import random

n, q = 100,20
series = [random.randint(0,n-1) for i in range(n)]

def generate_query(q, n):
    q1_1 = [random.randint(0,n-2) for i in range(q)]
    q1_2 = [random.randint(x, n - 2) for x in q1_1]
    q1 = [[1, q1_1[i], q1_2[i]] for i in range(q)]
    q2 = [[2, random.randint(0,n-1), random.randint(0,n-1)] for i in range(q)]
    select = [random.randint(0,3) for i in range(q)]
    queries = [q2[i] if (select[i] == 0) else q1[i] for i in range(q)]
    return queries

queries = generate_query(q, n)
print(series)
print(queries)