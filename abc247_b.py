N = int(input())
L = [list(input().split()) for _ in range(N)]

from collections import defaultdict
D = defaultdict(int)
for s, t in L:
    D[s] += 1
    D[t] += 1
for s, t in L:
    if s == t:
        if D[s] == 2:
            continue
        print('No')
        exit()
    else:
        if D[s] == 1:
            continue
        if D[t] == 1:
            continue
        print('No')
        exit()

print('Yes')
