import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

L = [0]*40

for i in A:
    for j in range(40):
        if (i >> j) & 1:
            L[j] += 1
            
X = [-1]*40
x = 0 

for i in range(int(math.log2(K))+1):
    if L[i] < N - L[i]:
        X[i] = 1
        x += 2 ** i
    else:
        X[i] = 0
        
ans = 0

if x <= K:
    for i in range(40):
        if X[i] == 0:
            ans += L[i] * 2 ** i
        if X[i] == 1:
            ans += (N - L[i]) * 2 ** i
    print(ans)
else:
    print()
    