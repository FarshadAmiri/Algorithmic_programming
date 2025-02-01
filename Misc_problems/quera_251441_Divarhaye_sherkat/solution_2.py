# n_rows = int(input())

# colored_rows = []

# for i in range(n_rows):
#     l, r = map(int, input().split())
#     colored_rows.append((l, r))

import random, time
n_rows = 10000000
colored_rows = [(random.randint(1, 90), random.randint(2, 100)) for _ in range(n_rows)]

tic = time.time()

def range_to_set(x_range):
    range_list = []
    r = x_range[0]
    l = x_range[1]
    for i in range(r, l):
        range_list.append(i)
    return set(range_list)

colored_rows_list = []
for i_range in colored_rows:
    colored_rows_list.append(range_to_set(i_range))

cv , ch = 0, 0
cv = 2 * n_rows

for row in range(n_rows + 1):

    if row == 0:
        ch += len(colored_rows_list[row])
        current = colored_rows_list[row]
    
    elif row == n_rows:
        ch += len(colored_rows_list[-1])

    else:
       previous = current
       current = colored_rows_list[row]

       new_c = (current | previous) - (current & previous)
       ch += len(new_c)

ct = cv + ch

print(ct)

tac = time.time()
time_spent = tac - tic

print(f"{time_spent:.3} seconds took!")