from itertools import combinations
N, A = map(int,input().split())
X = list(map(int,input().split()))
X = [i-A for i in X]

dp = [[0]*5000 for i in range(N+1)]
s = 2500
dp[0][s] = 1

for i in range(N):
    for j in range(5000):
        if dp[i][j] == 0:
            continue
        dp[i+1][j] += dp[i][j]
        dp[i+1][j+X[i]] += dp[i][j]

print(dp[N][s] - 1)