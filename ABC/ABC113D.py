H, W, K = map(int, input().split())

mod = 10 ** 9 + 7

dp = [[0]*W for i in range(H+1)]
dp[0][0] = 1

cnt = [0] * (W-1)
num = 0

for i in range(2**(W-1)):
    tmp = -2
    tmp_L = [0] * (W-1)
    for j in range(W-1):
        if (i >> j) & 1:
            if j - tmp == 1:
                break
            else:
                tmp = j
                tmp_L[j] += 1
    else:
        for k in range(W-1):
            cnt[k] += tmp_L[k]
        num += 1

cnt += [0]

for i in range(H):
    for j in range(W):
            dp[i+1][j] += dp[i][j] * (num - cnt[j] - cnt[j-1])
            dp[i+1][j] %= mod
            if j + 1 < W:
                dp[i+1][j+1] += dp[i][j] * cnt[j]
                dp[i+1][j+1] %= mod
            if j - 1 >= 0:
                dp[i+1][j-1] += dp[i][j] * cnt[j-1]
                dp[i+1][j-1] %= mod

print(dp[H][K-1])
