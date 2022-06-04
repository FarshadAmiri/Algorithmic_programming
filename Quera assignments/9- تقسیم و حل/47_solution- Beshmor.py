import sys
sys.setrecursionlimit(100) # maximum recusion is log(exp)

T = int(input())
while T :
    T -= 1

    # input
    inp = list(map(int, input().split()))
    a = list(map(int, input().split()))
    n = inp[0] # length of array
    k = inp[1] # K

    # calcuating ps
    ps = [0] * (n+1)
    ps[0] = 0
    for i in range(n):
        ps[i+1] = ps[i] + a[i] # ps[i] = a[0] + ... + a[i-1] --> ps[i] + a[i] = a[0] + ... + a[i] = ps[i+1]
    ps.sort()
    print(ps)

    ans = 0
    for i in range(1,n+1):
        st = -1
        en = i
        # binary search to find last index 'j' in ps that ps[i] - ps[j] > k
        while st != en-1 :
            mid = int((st+en)/2)
            if ps[i] - ps[mid] <= k:
                en = mid
            else:
                st = mid
        ans += en
    print(ans)