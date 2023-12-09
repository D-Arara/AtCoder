from heapq import heappop, heappush
from bisect import bisect_left
N, M = map(int, input().split())
S = []
T = []
for i in range(M):
    t, w, s = map(int, input().split())
    S.append((t, w, s))
    T.append(t)

res = [0] * N
r = list(range(N))
q = [[] for _ in range(M+1)]

for i in range(M):
    t, w, s = S[i]
    for j in q[i]:
        heappush(r, j)
    if not r:
        continue
    n = heappop(r)
    res[n] += w
    m = bisect_left(T, t+s)
    q[m].append(n)
print(*res, sep='\n')
    