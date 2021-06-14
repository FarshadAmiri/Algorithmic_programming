from math import floor
number = int(input())


def digits_sum(number):
    if number == 0:
        return 0
    else:
        return digits_sum(floor(number/10)) + number%10


print(digits_sum(number))