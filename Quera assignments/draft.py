l = [1,2,3,4,5,6,7,8,9]

k = 0
i = 8

while True:
    try:
        l[8-k] = 0
        k += 1
    except:
        break

print(l)