# 3 7
# 2 5
# 3 2
# 8 12
n, en = map(int, input().split())
fruits = []
for i in range(n):
    t, g = map(int, input().split())
    fruits.append((t, g-t))
print(fruits)
for f in fruits:
    if f[1] <= 0:
        fruits.remove(f)
fruits.sort(key= lambda x: x[0])
print(fruits)

def eat(fruits, consumed, en):
    diff = 0
    for i in consumed:
        fruits.remove(i)
    for t, g in fruits:
        if en >= t:
            en += g
            diff += g
            # fruits.remove((t, g))
            consumed.append((t, g))
        # print(f'diff: {diff}')
        # print(f'en: {en}')
        # print(f'fruits: {fruits}')
        # print()
    return (consumed, en, diff)

diff_list = [1,1]
consumed = []
while (diff_list[-1]>0) or (diff_list[-2]>0) or (diff_list[-3]>0) or (diff_list[-4]>0):
    fruits_2 = fruits.copy()
    consumed, en, diff = eat(fruits_2, consumed, en)
    diff_list.append(diff)

print(en)

