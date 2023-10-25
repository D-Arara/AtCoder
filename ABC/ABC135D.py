S = input()
N = len(S)
mod = 10 ** 9+ 7

dp = [[0]*13 for i in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(13):
        if dp[i][j] == 0:
            continue
        if S[i] == '?':
            for k in range(10):
                l = (10 * j + k) % 13
                dp[i+1][l] += dp[i][j]
                dp[i+1][l] %= mod
        else:
            l = (10 * j + int(S[i])) % 13
            dp[i+1][l] += dp[i][j]
            
print(dp[N][5])