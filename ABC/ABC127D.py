from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

D = defaultdict(int)
for a in A:
    D[a] += 1

for i in range(M):
    B, C = map(int, input().split())
    D[C] += B

L = sorted(D.keys(), reverse=True)
ans = 0
cnt = 0

for i in L:
    if cnt + D[i] >= N:
        ans += i * (N - cnt)
        print(ans)
        exit()
    else:
        ans += i * D[i]
        cnt += D[i]