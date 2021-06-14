import sys
sys.setrecursionlimit(10**6)

x = int(input())

def f(n):
  if n == 0:
    return 5
  if n%2 == 0:
    return f(n-1) - 21
  a = f(n-1)
  return a**2

print(f(x))