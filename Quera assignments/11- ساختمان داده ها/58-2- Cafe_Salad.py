from collections import defaultdict

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
names = {name:n for n,name in enumerate(sorted_names)}
id_to_name = {n:name for n,name in enumerate(sorted_names)}
# print(names)

marks = [False for i in range(len(names))]
revoke_date = defaultdict(list)


def do_this_day(day):
    global days, ids, marks, names, ops
    kicked = []
    for i,j in ops[day]:
        marks[names[i]] = True
        revoke_date[j + day - 1].append(names[i])

    for i in revoke_date[day]:
        if marks[i] == True:
            kicked.append(i)
            marks[i] = False
    for i in sorted_names:
        if marks[names[i]] == True:
            kicked.append(names[i])
            marks[names[i]] = False
            break

    kicked_names = []
    for i in kicked:
        kicked_names.append(id_to_name[i])

    kicked_names.sort()
    print(*kicked_names)



for i in range(q):
    do_this_day(i)