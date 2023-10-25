N, Ma, Mb = map(int, input().split())

A = list()
B = list()
C = list()

for i in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

Sa = sum(A) + 1
Sb = sum(B) + 1

INF = float('INF')
dp = [[[INF]*Sb for i in range(Sa)] for i in range(N+1)]

dp[0][0][0] = 0

for i in range(N):
    for j in range(Sa):
        for k in range(Sb):
            if dp[i][j][k] == INF:
                continue
            dp[i+1][j][k] = min(dp[i][j][k], dp[i+1][j][k])
            dp[i+1][j+A[i]][k+B[i]] = min(dp[i][j][k] + C[i], dp[i+1][j+A[i]][k+B[i]])

ans = INF

for i in range(1,Sa):
    for j in range(1,Sb):
        if Ma * j != Mb * i:
            continue
        ans = min(ans,dp[N][i][j])

if ans != INF:
    print(ans)
else:
    print(-1)