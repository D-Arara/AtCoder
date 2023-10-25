from itertools import accumulate

N, K = map(int, input().split())
D = list(map(int, input().split()))

E = D[::-1]

mD = [[] for i in range(N+1)]
mE = [[] for i in range(N+1)]

for i in range(N):
    if D[i] < 0:
        for j in range(i,N):
            mD[j].append(D[i])

for i in range(N):
    if E[i] < 0:
        for j in range(i,N):
            mE[j].append(E[i])

mD = mD
mE = mE
            
aD = [0] + list(accumulate(D))
aE = [0] + list(accumulate(E))

ans = 0

for i in range(min(K+1, N+1)):
    for j in range(min(K+1, N+1)-i):
        tmp = aD[i] + aE[j]
        L = sorted(mD[i-1] + mE[j-1])
        tmp -= sum(L[:min(len(L), K-i-j)])
        ans = max(ans, tmp)

print(ans)