n = int(input())
agencies = {}
for i in range(n):
    agencies[input()] = i
# print(agencies)
q = int(input())
info = []
for i in range(q):
    info.append(agencies[input()])
# print(info)

n_list = list(range(n))
movements = 0

for i in info:
    try:
        n_list.remove(i)
    except:
        continue
    if len(n_list) == 0:
        movements += 1
        n_list = list(range(n))
        n_list.remove(i)
print(movements)












