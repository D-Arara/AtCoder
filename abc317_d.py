N = int(input())

L = []
cnt = 0
for i in range(N):
    X, Y, Z = map(int, input().split())
    cnt += Z
    if X > Y :
        L.append((0, Z))
    else:
        L.append(((Y-X+1)//2, Z))

inf = 1 << 61
dp = [[inf] * (10**5+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    C, Z = L[i]
    for j in range(10**5+1):
        if dp[i][j] == inf:
            continue
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][j+Z] = min(dp[i][j] + C, dp[i+1][j+Z])

print(min(dp[-1][cnt//2+1:]))
