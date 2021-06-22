import numpy as np

n,k = map(int, input().split())
pattern = ''
for i in range(n):
    pattern = pattern + input() + '\n'
pattern = pattern.strip()

pattern_arr = np.zeros(shape=(n,n))
d = {'.': 0, '*': 1}
if n == 2:
    pattern_arr[0,0]= d[pattern[0]]
    pattern_arr[0,1] = d[pattern[1]]
    pattern_arr[1,0]= d[pattern[3]]
    pattern_arr[1,1] = d[pattern[4]]
if n == 3:
    pattern_arr[0,0]= d[pattern[0]]
    pattern_arr[0,1] = d[pattern[1]]
    pattern_arr[0,2]= d[pattern[2]]
    pattern_arr[1,0] = d[pattern[4]]
    pattern_arr[1,1] = d[pattern[5]]
    pattern_arr[1,2] = d[pattern[6]]
    pattern_arr[2,0] = d[pattern[8]]
    pattern_arr[2,1] = d[pattern[9]]
    pattern_arr[2,2] = d[pattern[10]]

def fractalize( n, k, older_array, pattern):
    new_array = np.zeros(shape= (n**k, n**k))
    for index, value in np.ndenumerate(older_array):
        if value == 0:
            if n == 2:
                new_array[n * index[0]][n * index[1]] = pattern[0][0]
                new_array[n * index[0] + 1][n * index[1]] = pattern[1][0]
                new_array[n * index[0]][n * index[1] + 1] = pattern[0][1]
                new_array[n * index[0] + 1][n * index[1] + 1] = pattern[1][1]
            if n == 3:
                new_array[n * index[0]][n * index[1]] = pattern[0][0]
                new_array[n * index[0]][n * index[1] + 1] = pattern[0][1]
                new_array[n * index[0]][n * index[1] + 2] = pattern[0][2]
                new_array[n * index[0] + 1][n * index[1]] = pattern[1][0]
                new_array[n * index[0] + 1][n * index[1] + 1] = pattern[1][1]
                new_array[n * index[0] + 1][n * index[1] + 2] = pattern[1][2]
                new_array[n * index[0] + 2][n * index[1]] = pattern[2][0]
                new_array[n * index[0] + 2][n * index[1] + 1] = pattern[2][1]
                new_array[n * index[0] + 2][n * index[1] + 2] = pattern[2][2]
        if value == 1:
            if n == 2:
                new_array[n * index[0]][n * index[1]] = 1
                new_array[n * index[0] + 1][n * index[1]] = 1
                new_array[n * index[0]][n * index[1] + 1] = 1
                new_array[n * index[0] + 1][n * index[1] + 1] = 1
            if n == 3:
                new_array[n * index[0]][n * index[1]] = 1
                new_array[n * index[0]][n * index[1] + 1] = 1
                new_array[n * index[0]][n * index[1] + 2] = 1
                new_array[n * index[0] + 1][n * index[1]] = 1
                new_array[n * index[0] + 1][n * index[1] + 1] = 1
                new_array[n * index[0] + 1][n * index[1] + 2] = 1
                new_array[n * index[0] + 2][n * index[1]] = 1
                new_array[n * index[0] + 2][n * index[1] + 1] = 1
                new_array[n * index[0] + 2][n * index[1] + 2] = 1
    return new_array

def array_to_str(array):
    result = ''
    for i in array:
        for j in i:
            if j == 0:
                result = result + '.'
            if j == 1:
                result = result + '*'
        result = result + '\n'
    result = result.strip()
    return result

if k == 1:
    print(array_to_str(pattern_arr))
if k >1:
    older_array = pattern_arr
    for i in range(2,k+1):
        older_array = fractalize(n=n, k=i, older_array=older_array, pattern=pattern_arr)
    print(array_to_str(older_array))
