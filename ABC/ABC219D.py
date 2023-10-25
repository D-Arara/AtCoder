N = int(input())
X, Y = map(int, input().split())

M = 301

dp = [[[M]*(Y+1) for i in range(X+1)] for j in range(N+1)]
dp[0][0][0] = 0

for n in range(N):
    A, B = map(int, input().split())
    for x in range(X+1):
        for y in range(Y+1):
            if dp[n][x][y] == M:
                continue
            dp[n+1][x][y] = min(dp[n][x][y], dp[n+1][x][y])
            dp[n+1][min(X, x+A)][min(Y, y+B)] = min(dp[n+1][min(X, x+A)][min(Y, y+B)], dp[n][x][y] + 1)

if dp[N][X][Y] != M:
    print(dp[N][X][Y])
else:
    print(-1)