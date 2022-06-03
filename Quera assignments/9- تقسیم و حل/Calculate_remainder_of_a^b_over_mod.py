# The problem is to calculate remainder of a^b over mod.
# All following solutions are correct, but they have different time complexity orders.

# Source: Advanced Algorithmic Programming Course by Quera.ir - Divide and Conquer Algorithms.
# https://quera.org/college/3016/chapter/8240/lesson/27775/?comments_page=1&comments_filter=ALL


import math
import time


def simplest_solution(a, b, mod):
    return (a**b) % mod


# O(b)
def simple_mod(a, b, mod):
    result = 1
    for i in range(b):
        result *= a
        result = result % mod
    return result



# O(b)
res = 1
def recursive_mod(a, b , mod):
    global res
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        res = recursive_mod(a, math.floor(b/2), mod) * recursive_mod(a, math.ceil(b/2), mod)
        res = res % mod
    return res


# O(log(b))
def optimized_mod(a, b, mod):
    if b == 0:
        return 1
    result = optimized_mod(a, math.floor(b / 2), mod)
    if b % 2 == 1:
        result = ((result*result) % mod) * a
    else:
        result = result * result
    result = result % mod
    return result

# --------------------------------
# Inputs
a, b = 2545122, 464514
mod = 1915151
# --------------------------------

t1 = time.time()
print('(a**b) % mod = ', simplest_solution(a, b, mod))
t_simplest_solution = time.time() - t1


t2 = time.time()
print('simple_mod(a,b, mod) = ', simple_mod(a,b, mod))
t_simple_mod = time.time() - t2

t3 = time.time()
print('recursive_mod(a, b , mod) = ',recursive_mod(a, b , mod))
t_recursive_mod = time.time() - t3

t4 = time.time()
print('optimized_mod(a, b, mod) = ',optimized_mod(a, b, mod))
t_optimized_mod = time.time() - t4


print()
print(f't_simplest_solution = {t_simplest_solution:.5f}')
print(f't_simple_mod = {t_simple_mod:.5f}')
print(f't_recursive_mod = {t_recursive_mod:.5f}')
print(f'optimized_mod(a, b, mod) = {t_optimized_mod:.5f}')