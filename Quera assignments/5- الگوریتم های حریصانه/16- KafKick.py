n, k = map(int, input().split())
numbers = list(map(int, input().split()))

if k == 1:
    print(max(numbers))

if k >= 3:
    print(min(numbers))

if k == 2:
    if (numbers[0] == min(numbers)) or (numbers[-1] == min(numbers)):
        print(min(numbers))
    else:
        print(min(numbers[0], numbers[-1]))


