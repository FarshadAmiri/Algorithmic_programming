def transformable(w1, w2):
    n = len(str(w1))
    w1, w2 = str(w1), str(w2)
    for x in range(1,n+1):
        w1_t = w1[:x][::-1] + w1[x:]
        w2_t = w2[:x][::-1] + w2[x:]
        if (w1 == w2_t) or (w1_t == w2):
            return True
    return False

print(transformable(54312, 21345))