n = int(input())
seq = list(map(int, input().split()))

max_sum = dict()
max_sum[0] = seq[0]

for i in range(1,len(seq)):
    max_sum[i] = max(seq[i], max_sum[i-1] + seq[i])

print(max(max_sum.values()))