n , q = input().split(' ')
n , q = int(n) , int(q)
c = input().split(' ')
c =[int(i) for i in c]
d = []

for i in range(0,q):
    d.append(int(input()))


result = []
for i in range(0,q):
    sad_people = 0
    for j in range(0,n):
        if d[i]>c[j]:
            sad_people += 1
    result.append(sad_people)

for i in range(0,q):
    print(result[i])

