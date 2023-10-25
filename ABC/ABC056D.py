N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

dp = [[False]*(K+1) for i in range(N+1)]
dp[0][0] = True

num = 0

for i in range(N):
    for j in range(K+1):
        if not dp[i][j]:
            continue
        dp
