# Gray code
# Recursive algorithms

n = int(input())


def gray(n):
    if n == 1:
        return ['0', '1']
    else:
        result = []
        for i in gray(n-1):
            result.append('0' + i)
        result_reversed = result.copy()
        result_reversed.reverse()
        for i in result_reversed:
            i = '1' + i[1:]
            result.append(i)
        return result


for i in gray(n):
    print(i)


