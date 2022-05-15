n, k = map(int , input().split())

def num_inversions(series):
    k = 0
    for i,n in enumerate(series):
        for j,m in enumerate(series[i+1:]):
            if n > m:
                k += 1
    return k

ans = 0
current_permut = []

def build(n,k):
    global ans
    global current_permut
    if len(current_permut) == n:
        if num_inversions(current_permut) == k:
            ans += 1

    else:
        for i in range(1,n+1):
            if i not in current_permut:
                current_permut.append(i)
                build(n, k)
                current_permut = current_permut[:-1]
    return ans

print(build(n, k))