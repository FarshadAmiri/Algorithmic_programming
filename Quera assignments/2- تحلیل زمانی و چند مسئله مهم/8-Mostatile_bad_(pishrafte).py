from math import floor as fl
n = int(input())

bound = fl((fl(n/2)+1)/2)
answer = bound * (bound + 1) - fl(n/2) * bound + fl(n/3) - bound
k = fl(fl(n/3)/2)
answer += (n + 1) * k - 3 * k * (k + 1)

if fl(n/3)%2 == 1:
    answer += fl((n - 3 * (2 * k + 1))/2)

mod = int(1e9 + 7)

print(answer%mod)