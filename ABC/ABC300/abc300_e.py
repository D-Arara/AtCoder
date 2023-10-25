N = int(input())
mod = 998244353
re = pow(5, mod-2, mod)

dp = [[[0] * 36 for _ in range(54)] for _ in range(72)]
dp[0][0][0] = 1

res = 0
for i in range(72):
    tmp2 = 2 ** i
    for j in range(54):
        tmp3 = 3 ** j
        for k in range(36):
            if i == j == k == 0:
                continue
            if tmp2 * tmp3 * 5 ** k > N:
                break
            tmp = ((dp[i-1][j][k] + dp[i][j-1][k] + dp[i-2][j][k] + dp[i][j][k-1] + dp[i-1][j-1][k]) * re) % mod
            if tmp2 * tmp3 * 5 ** k == N:
                res += tmp
                res %= mod
            else:
                dp[i][j][k] = ((dp[i-1][j][k] + dp[i][j-1][k] + dp[i-2][j][k] + dp[i][j][k-1] + dp[i-1][j-1][k]) * re) % mod

print(res)