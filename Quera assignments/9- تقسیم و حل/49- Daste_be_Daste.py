n = int(input())
people = list(map(int, input().split()))


ans = 0
def solve(people):
    global ans

    if len(people) == 1:
        ans+= people[0]
        return

    mid = int(len(people) / 2)
    g1 = people[:mid]
    g2 = people[mid: ]

    if sum(g1) >= sum(g2):
        #g2 should ne eliminated
        ans += max(g2)
        solve(g1)
    else:
        ans += max(g1)
        solve(g2)

solve(people)
print(ans)