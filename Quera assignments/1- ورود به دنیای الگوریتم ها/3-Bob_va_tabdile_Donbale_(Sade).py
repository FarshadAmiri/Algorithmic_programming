n,k = map(int, input().split(' '))
donbale = list(map(int, input().split(' ')))

results = []
for i in range(-100-(n-1)*k,101+(n-1)*k):
    donbale_farzi = []
    for j in range(n):
        donbale_farzi.append(i+j*k)
    required_steps = 0
    for m in range(n):
        required_steps += abs(donbale_farzi[m] - donbale[m])
    results.append(required_steps)

print(min(results))
