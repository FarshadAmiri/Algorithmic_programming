n = int(input())
people = list(map(int, input().split()))

ans = [0 for i in range(2**n)]


def solve(people, l, r):
    global ans

    if r - l == 1:
        ans[l] += people[l]
        return

    mid = int((r + l) / 2)
    # if r - l > 3:
    max_l_mid = max(people[l : mid])
    max_mid_r = max(people[mid : r])

    for i in range(l, mid):
        ans[i] += max_mid_r
    solve(people, l, mid)
    for i in range(mid, r):
        ans[i] += max_l_mid
    solve(people, mid, r)


solve(people, 0, len(people))
print(max(ans))