N, S = map(int, input().split())
L = [tuple(map(int, input().split())) for i in range(N)]
dp = [['n'] * (S+1) for i in range(N+1)]
dp[0][0] = ''
for i in range(N):
    A, B = L[i]
    for j in range(S+1):
        if dp[i][j] == 'n':
            continue
        if j + A <= S:
            dp[i+1][j+A] = dp[i][j] + 'A'
        if j + B <= S:
            dp[i+1][j+B] = dp[i][j] + 'B'
if dp[-1][-1] != 'n':
    print(dp[-1][-1])
else:
    print('Impossible')