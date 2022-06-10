n = int(input())
role_models = list(map(int, input().split()))

role_models = [i-1 for i in role_models]
ppl = [i for i in range(n)]
ppl2 = [i for i in range(n)]
counter = [0 for i in range(n)]

for i in role_models:
    counter[i] += 1


def solve(subset, removed):
    global counter, ppl2

    remove_queue = []
    for id, i in enumerate(counter):
        if (i == 0) and (id not in removed):
            remove_queue.append((id, ppl2[id]))
            removed.append(id)
    for id, i in remove_queue:
        subset.remove(i)
        counter[role_models[id]] -= 1

    if len(remove_queue) == 0:
        print(len(subset))
        print(*[i+1 for i in subset])
        return

    solve(subset, removed)



solve(ppl, [])