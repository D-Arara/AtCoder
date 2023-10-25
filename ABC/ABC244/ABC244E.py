N, M, K, S, T, X= map(int, input().split())
mod = 998244353
node = [[] for i in range(N)]

for i in range(M):
    U, V = map(int, input().split())
    node[U-1].append(V-1)
    node[V-1].append(U-1)

dp = [[[0, 0] for i in range(N)] for i in range(K+1)]
dp[0][S-1][0] = 1


for i in range(K):
    for j in range(N):
        for k in range(2):
            if dp[i][j][k] == 0:
                continue
            for l in node[j]:
                if l == X - 1:
                    dp[i+1][l][k^1] += dp[i][j][k]
                    dp[i+1][l][k^1] %= mod
                else:
                    dp[i+1][l][k] += dp[i][j][k]
                    dp[i+1][l][k] %= mod
                    
print(dp[K][T-1][0])