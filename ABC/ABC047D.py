from collections import defaultdict
N, T = map(int,input().split())
A = list(map(int,input().split()))
M = A[-1]

D = defaultdict(int)

for i in range(N-2,-1,-1):
    if A[i] > M:
        M = A[i]
    else:
        D[M-A[i]] += 1

key = max(D.keys())
print(D[key])