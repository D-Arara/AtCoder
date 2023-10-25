N = int(input())

inf = 10 ** 5 + 1
dp = [inf]*(N+1)
dp[0] = 0

for i in range(N+1):
    for j in range(N):
        if i + (6 ** j) > N:
            break
        dp[i+(6**j)] = min(dp[i]+1, dp[i+(6**j)])
    for j in range(1,N):
        if i + (9 ** j) > N:
            break
        dp[i+(9**j)] = min(dp[i]+1, dp[i+(9**j)])

print(dp[N])