import sys
sys.setrecursionlimit(1000000000)

n = int(input())
people = list(map(int, input().split()))

ans = 0
def solve(people, l, r, prize):
    global ans

    # if (l == 0) and (r == len(people)):
    #     prize = 0
    if r - l == 1:
        if sum(prize) > ans:
            ans = sum(prize)
        return

    mid = int(len(people) / 2)
    try:
        prize.append(max(people[mid:r]))
    except:
        pass
    solve(people, l, mid, prize)
    prize.pop()
    try:
        prize.append(max(people[l:mid]))
    except:
        pass
    solve(people, mid, r, prize)
    prize.pop()


solve(people, 0 , len(people), [])
print(ans)