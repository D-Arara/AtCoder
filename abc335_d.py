N = int(input())

L = [[0] * N for _ in range(N)]
L[(N+1)//2-1][(N+1)//2-1] = 'T'
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

x, y = 0, 0
r = 0
for i in range(1,N**2):
    L[x][y] = i
    if x + d[r][0] < 0 or N <= x + d[r][0] or y + d[r][1] < 0 or N <= y + d[r][1] or L[x+d[r][0]][y+d[r][1]] != 0:
        r = (r+1) % 4
    x += d[r][0]
    y += d[r][1]

for l in L:
    print(*l)