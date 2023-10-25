X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

L = list()

for a in A:
    for b in B:
        L.append(a+b)

L.sort(reverse = True)

if len(L) > K:
    L = L[:K+1]

ans = []

for l in L:
    for c in C:
        ans.append(l+c)
        
ans.sort(reverse = True)

for i in range(K):
    print(ans[i])