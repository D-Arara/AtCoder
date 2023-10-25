from collections import defaultdict

N, K = map(int,input().split())
A = list(map(int,input().split()))

Sa = [0]*N
for i in range(N):
    Sa[i] = Sa[i-1] + A[i]

Sa = [0] + Sa

D = defaultdict(int)

for i in Sa:
    D[i] += 1

ans = 0

for i in range(N):
    if D[Sa[i]+K] > 0:
        ans += D[Sa[i]+K]
        if K == 0:
            ans -= 1
    D[Sa[i]] -= 1 

print(ans)