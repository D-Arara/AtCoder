N = int(input())
mod =  998244353

dp = [[0] * 9 for i in range(N-1)]
dp = [[1] * 9] + dp

for i in range(1,N):
    for j in range(9):
        if j != 0:
            dp[i+1][j-1] += [i][j]
            dp[i+1][j-1] %= mod
        if j != 8:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        
ans = 0
for i in dp[N-1]:
    ans += i
    ans %= mod
print(ans)