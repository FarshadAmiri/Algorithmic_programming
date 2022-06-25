# q = int(input())
# ops = []
# names = set()
#
# for i in range(q):
#     l = input().split()
#     n = 1
#     day_ops = []
#     while n <= int(l[0]):
#         day_ops.append((l[2 * n - 1], int(l[2 * n])))
#         names.add(l[2 * n - 1])
#         n += 1
#     ops.append(day_ops)
#
#
# names = sorted(names)
# print(ops)
# print(names)
import heapq

q = 4
ops = [[('hamid', 1), ('ali', 4), ('rayan', 2)], [('asgharparande', 2), ('kamid', 3)], [('keytwo', 2), ('arezoo', 2)], [('keyone', 1)]]
names = ['ali', 'arezoo', 'asgharparande', 'hamid', 'kamid', 'keyone', 'keytwo', 'rayan']
names = sorted(names)
names = {name:n for n,name in enumerate(names)}
print(names)

days = []
ids = []
marks = [False for i in range(len(names))]
revoke_date = {}

def do_this_day(day):
    global days, ids, marks, names, ops
    kicked = []
    for i,j in ops[day]:
        heapq.heappush(days, j + day - 1)
        heapq.heappush(ids, names[i])
        if revoke_date[j + day - 1]:
            revoke_date[j + day - 1].append(names[i])
        else:
            revoke_date[j + day - 1] = names[i]
    while min(days) == day:
        heapq.heappop(days)



for i in range(q):
    do_this_day(i)