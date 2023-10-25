import sys
input = sys.stdin.readline
import bisect

N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]

V = sum(x[1] for x in vw)

if N <= 30:
    ans = 0
    for i in range(2**N):
        w = 0
        v = 0
        for j in range(N):
            if (i >> j) & 1:
                v += vw[j][0]
                w += vw[j][1]
        if w <= W:
            ans = max(ans,v)
    print(ans)

elif W < V:
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i, (v, w) in enumerate(vw):
        for j in range(W + 1):
            dp[i + 1][j] = dp[i][j]
            if j - w >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)

    print(dp[-1][-1])

else:
    INF = 1 << 60
    dp = [INF] * (V + 1)
    dp[0] = 0

    for v, w in vw:
        dp_tmp = dp[:]
        for j in range(1, V + 1):
            idx_prev = max(0, j - v)
            dp_tmp[j] = min(dp[j], dp[idx_prev] + w)
        dp = dp_tmp

    print(bisect.bisect_right(dp, W) - 1)