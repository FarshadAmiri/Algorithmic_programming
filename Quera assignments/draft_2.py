x = [1,5,4,7,9,3,4,6,5,2]

for i in x:
    for j in range(i - 2, i + 3):
        if j == 6:
            break
        print(j)