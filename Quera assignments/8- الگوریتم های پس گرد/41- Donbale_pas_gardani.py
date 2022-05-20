n = int(input())

series = []
for k in range(n):
    series.append(list(map(int, input().split()))[1:])

# print(series)

numbers = set([item for sublist in series for item in sublist])
mark = dict()
for i in numbers:
    mark[i] = False

result = 0

def build(n, current_seq, sequences):
    global result
    global mark
    if current_seq == n:
        return 1
    result = 0

    for i in range(len(sequences[current_seq])):
        x = sequences[current_seq][i]
        if mark[x] == False:
            mark[x] = True
            result += build(n, current_seq+1, sequences)
            mark[x] = False
    return result

print(build(n, 0, series))