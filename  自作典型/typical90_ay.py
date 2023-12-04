from collections import defaultdict
from bisect import bisect_right
N, K, P = map(int, input().split())
A = list(map(int, input().split()))
x = N // 2
y = (N + 1) // 2
X = A[:x]
Y = A[x:]
D = defaultdict(list)
for i in range(2**x):
    cnt = 0
    tmp = 0
    for j in range(x):
        if (i >> j) & 1 == 1:
            cnt += 1
            tmp += X[j]
    D[cnt].append(tmp)

for k in D.keys():
    D[k].sort()
    
res = 0
for i in range(2**y):
    cnt = 0
    tmp = P
    for j in range(y):
        if (i >> j) & 1 == 1:
            cnt += 1
            tmp -= Y[j]
    if len(D[K-cnt]) == 0:
        continue
    res += bisect_right(D[K-cnt], tmp)

print(res)
    