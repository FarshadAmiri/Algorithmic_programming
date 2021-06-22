# My way: (I prefer recursive solutions too)
# import math
# n = int(input())
#
# ways = []
# for a in range(n+1):
#     for b in range(int(n/2)+1):
#         for c in range(int(n/5)+1):
#             if a + b*2 + c*5 == n:
#                 ways.append((a,b,c))
#
# num_ways = 0
# for i in ways:
#     num = math.factorial(i[0] + i[1] + i[2]) / ((math.factorial(i[0])) *  (math.factorial(i[1])) * (math.factorial(i[2])))
#     num_ways += num
# print(int(num_ways))

# ---------------------------------------
# Recursive solution-1
result = 0
def step(n):
  if n < 0:
    return 0
  if n == 0:
    return 1

  return (step(n - 1) +
          step(n - 2) +
          step(n - 5))

n=int(input())
print(step(n))

# ------------------------------
# Recursive solution-2

# n = int(input())
# def findStep(n):
#     if (n < 0):
#       return 0
#     if (n == 1 or n == 0):
#         return 1
#     elif (n == 2):
#         return 2
#     elif (n == 3):
#         return 3
#     elif (n == 4):
#         return 5
#
#     else:
#         return findStep(n - 5) + findStep(n - 2) + findStep(n - 1)
#
# print(findStep(n))
# ---------------------------------------------------------
# Recursive solution-2 (modified) --- It's actually the same as first recursive solution.
# n = int(input())
# def findStep(n):
#     if (n < 0):
#       return 0
#     if (n == 1 or n == 0):
#         return 1
#
#     else:
#         return findStep(n - 5) + findStep(n - 2) + findStep(n - 1)
#
# print(findStep(n))
# ---------------------------------------------------------
# recursive solution-3
# n = int(input())

# ans = 0
# def f(n, place=0):
#     global ans
#     if place > n:
#         return
#     if place == n:
#         ans += 1
#
#     f(n, place + 1)
#     f(n, place + 2)
#     f(n, place + 5)
#
# f(n)
# print(ans)