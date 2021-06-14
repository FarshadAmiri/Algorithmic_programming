import time

n = int(input())

t1 = time.time()

# My solution:
seq = {}
for i in range(1, n+1):
    seq['s' + str(i)] = ''
    for j in range(1, n+1 ):
        seq['s' + str(i)] += str(j) * n**(n-i)
    seq['s' + str(i)] *= n**(i-1)

for j in range(len(seq['s1'])):
    sequence = ''
    for i in range(1, n+1):
        sequence += seq['s' + str(i)][j]
        sequence += ' '
    print(sequence.strip())

t2 = time.time()



# A recursive solution
def func(A, n, m):
    if n == 0:
        print(*A, )
        return

    for i in range(m):
        newA = A.copy()
        newA.append(i + 1)
        func(newA, n - 1, m)

func([], n, n)


print(t2 - t1)
print(time.time() - t2)

# My way was about twice more time-effiecient.