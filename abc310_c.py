N = int(input())

S = [tuple(input()) for _ in range(N)]
cnt = 0

from collections import defaultdict
D = defaultdict(int)
for s in S:
    D[s] += 1
    D[s[::-1]] += 1
for k in D.keys():
    if k == k[::-1]:
        cnt += 1
    else:
        cnt += 1/2
print(int(cnt))