from bisect import bisect as upper_bound

t = int(input())
series = []

for i in range(t):
    _ , k = map(int, input().split())
    series.append((list(map(int ,input().split())), k))

def findCnt(arr, n, k):
    ans = 0
    for i in range(1,n):
        arr[i] += arr[i - 1]
        if (arr[i] > k or arr[i] < -1 * k):
            ans+=1

    if (arr[0] > k or arr[0] < -1 * k):
        ans+=1
    arr=sorted(arr)

    for i in range(n):
        ans += n - upper_bound(arr,arr[i] + k)
    return ans


for serie, k in series:
    print(findCnt(serie, len(serie), k))
