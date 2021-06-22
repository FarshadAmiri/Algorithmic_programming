# x = int(input())
# n = int(input())
x = 100
n = 2

result = 0
def next_round(x,i):
    global result
    global n
    if x < 0:
        result += 0
    if (x == 1) or (x == 0):
        result += 1
    for j in range(i, int(x ** (1/n)) + 1):
        next_round(x - i ** n, j+1)
    return result
print(next_round(x,i=1))