from collections import defaultdict
from itertools import accumulate, product

N, W = map(int, input().split())

D = defaultdict(list)

for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        base = w
    D[w].append(v)

w_list = []

for i in range(4):
    D[base+i].sort(reverse=True)
    D[base+i] = [0] + list(accumulate(D[base+i]))
    w_list.append(range(len(D[base+i])))

ans = 0

for i in product(*w_list):
    tmp = 0
    w = 0
    for j in range(4):
        tmp += D[base+j][i[j]]
        w += (base+j) * i[j]
    if w > W:
        continue
    ans = max(ans, tmp)

print(ans)