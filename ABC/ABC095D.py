from itertools import accumulate
from pkgutil import read_code

N, C = map(int, input().split())

X = []
V = []

for i in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)

reV = sorted(V, reverse=True)
reX = []

for i in X[::-1]:
    reX.append(C-i)

accumulate_V = list(accumulate(V))
accumulate_reV = list(accumulate(reV))

accumulate_V_2 = list(accumulate(V))
accumulate_reV_2 = list(accumulate(reV))

for i in range(N):
    accumulate_V[i] -= X[i]
    accumulate_reV[i] -= reX[i]
    accumulate_V_2[i] -= 2*X[i]
    accumulate_reV_2[i] -= 2*reX[i]

print(accumulate_V,accumulate_reV,accumulate_V_2,accumulate_reV_2)

ans = 0
M = [0] * (N+1)
tmp = 0
for i in range(N):
    tmp = max(accumulate_V[i], tmp)
    M[i+1] = tmp

reM = [0] * (N+1) 
tmp = 0
for i in range(N):
    tmp = max(accumulate_reV[i], tmp)
    reM[i+1] = tmp

m = [0] * (N+1)   
tmp = 0
for i in range(N):
    tmp = max(accumulate_V_2[i], tmp)
    m[i+1] = tmp

rem = [0] * (N+1)   
tmp = 0
for i in range(N):
    tmp = max(accumulate_reV_2[i], tmp)
    rem[i+1] = tmp

for i in range(N+1):
    ans = max(M[N-1-i]+m[i], ans)
    ans = max(reM[N-1-i]+rem[i], ans)

print(ans)