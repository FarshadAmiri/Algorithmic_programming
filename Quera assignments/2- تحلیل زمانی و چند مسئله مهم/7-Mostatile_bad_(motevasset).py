n = int(input())

answer = 0
for a in range(1, int(n/3)+1):
    mod = 1e9 + 7
    answer += int((n-3*a)/2) - max(0, int(n/2) - 2*a +1) + 1
print(int(answer%mod))