a = input()
b = input()


def subsets(word):
    subs = set()
    for mask in range(1<<len(word)):
        x = ''
        for i in range(len(word)):
            if mask & 1<<i:
                    x += word[i]
        subs.add(x)
    return subs


a_sub = subsets(a)
b_sub = subsets(b)

intersects = a_sub.intersection(b_sub)

lcs = max(intersects, key=len)

print(len(lcs))
print(lcs)