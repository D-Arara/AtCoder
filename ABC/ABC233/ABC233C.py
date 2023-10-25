from collections import defaultdict
N, X = map(int,input().split())

D = defaultdict(int)
D[1] += 1

for i in range(N):
    L = list(map(int,input().split()))
    tmp = defaultdict(int)
    for k, v in D.items():
        for j in L[1:]:
            if k * j > X:
                continue
            tmp[k*j] += v
    D = tmp

print(D[X])