S = input()
N = len(S)
mod = 998244353
dp = [[0] * (N+1) for _ in range(N+1)]

dp[0][0] = 1
for i in range(N):
    if S[i] == '(':
        dp[i+1][1:] = dp[i][:-1]
    if S[i] == ')':
        dp[i+1][:-1] = dp[i][1:]
    if S[i] == '?':
        for j in range(N+1):
            if j == 0:
                dp[i+1][0] = dp[i][1]
            elif j == N:
                dp[i+1][N] = dp[i][N-1]
            else:
                dp[i+1][j] = (dp[i][j-1] + dp[i][j+1]) % mod

print(dp[-1][0])
