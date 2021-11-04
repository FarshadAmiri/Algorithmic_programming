import numpy as np

m = 5
n = 6
# 5 rows & 6 cols


b = [[[0 for i in range(m)] for j in range(m)] for k in range(n)]

print(b)

bb = list(np.zeros(shape=(n,m,m)))

print(bb)