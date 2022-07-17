from collections import defaultdict
import heapq

q = int(input())
ops = []
names = set()

for i in range(q):
    l = input().split()
    n = 1
    day_ops = []
    while n <= int(l[0]):
        day_ops.append((l[2 * n - 1], int(l[2 * n])))
        names.add(l[2 * n - 1])
        n += 1
    ops.append(day_ops)



# q = 4
# ops = [[('hamid', 1), ('ali', 4), ('rayan', 2)], [('asgharparande', 2), ('kamid', 3)], [('keytwo', 2), ('arezoo', 2)], [('keyone', 1)]]
# names = ['ali', 'arezoo', 'asgharparande', 'hamid', 'kamid', 'keyone', 'keytwo', 'rayan']
sorted_names = sorted(names)
names_to_id = {name:n for n,name in enumerate(sorted_names)}
id_to_name = {n:name for n,name in enumerate(sorted_names)}
# print(names_to_id)

marks = [False for i in range(len(names_to_id))]
revoke_date = defaultdict(list)

days = []
ids = []

def do_this_day(day):
    global days, ids, marks, names_to_id, ops
    kicked = []
    for i,j in ops[day]:
        heapq.heappush(days, j + day - 1)
        revoke_date[j + day - 1].append(names_to_id[i])
        heapq.heappush(ids, names_to_id[i])
        if marks[names_to_id[i]] == False:
            marks[names_to_id[i]] = day + j - 1
        else:
            marks[names_to_id[i]] = max(marks[names_to_id[i]], day + j - 1)
    # print(f'revoke_date[{day}] = {revoke_date[day]}')
    for i in revoke_date[day]:
        try:
            heapq.heappop(days)
        except:
            continue
        try:
            ids.remove(i)
        except:
            continue
        kicked.append(id_to_name[i])
    heapq.heapify(ids)
    try:
        alpha_kicked = heapq.heappop(ids)
        revoke_date[marks[alpha_kicked]].remove(alpha_kicked)
        kicked.append(id_to_name[alpha_kicked])
    except:
        pass
    try:
        days.remove(marks[alpha_kicked])
    except:
        pass
    heapq.heapify(days)

    kicked.sort()
    print(*kicked)


for i in range(q):
    do_this_day(i)