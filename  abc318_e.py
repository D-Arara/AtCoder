from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

D = defaultdict(list)
for i in range(N):
    D[A[i]].append(i)
res = 0
for i in range(N+1):
    if len(D[i]) <= 1:
        continue
    for j in range(len(D[i])-1):
        res += (D[i][j+1] - D[i][j] - 1) * (j+1) * (len(D[i])-j-1)
print(res)

