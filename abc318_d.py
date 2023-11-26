N = int(input())
D = [list(map(int, input().split())) for _ in range(N-1)]
dp = [0] * 2 ** N
for i in range(2**N-1):
    for j in range(N-1):
        if not i & (1 << j):
            for k in range(j+1,N):
                if not i & (1 << k):
                    dp[i+(1<<j)+(1<<k)] = max(dp[i+(1<<j)+(1<<k)], dp[i]+D[j][k-j-1])

print(dp[-1])