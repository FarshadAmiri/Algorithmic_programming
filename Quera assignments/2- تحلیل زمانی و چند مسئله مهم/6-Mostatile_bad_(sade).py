n = int(input())

triangles_possible = 0
for i in range(1,n-1):
    for j in range(i,n-i):
        k = n - (i + j)
        if (i + j > k) and k >= j:
            triangles_possible += 1

print(triangles_possible)