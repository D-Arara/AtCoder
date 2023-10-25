H, N = map(int, input().split())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

inf = 10 ** 8 + 1
dp = [inf]*(H+1)
dp[0] = 0

for i in range(H+1):
    if dp[i] == inf:
        continue
    for j in range(N):
        if i + A[j] > H:
            dp[H] = min(dp[H], dp[i]+B[j])
        else:
            dp[i+A[j]] = min(dp[i+A[j]], dp[i]+B[j])

print(dp[H])