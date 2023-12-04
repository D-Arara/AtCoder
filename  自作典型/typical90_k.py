N = int(input())
L = [tuple(map(int, input().split())) for _ in range(N)]
L.sort()
dp = [[0] * 5001 for i in range(N+1)]
for i in range(N):
    D, C, S = L[i]
    for j in range(1,5001):
        if j > D or j - C < 0:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-1])
        else:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-1], dp[i][j-C] + S)
        
#print(dp[:8])
print(max(dp[-1]))
