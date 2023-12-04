N = int(input())
ABC = [list(map(int, input().split())) for _ in range(3)]
L = [[0] * 46 for i in range(3)]
for i in range(3):
    for j in range(N):
        L[i][ABC[i][j]%46] += 1
res = 0
for i in range(46):
    for j in range(46):
        res += L[0][i] * L[1][j] * L[2][(46-i-j)%46]
print(res)