from collections import deque
N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

Ax -= 1
Ay -= 1
Bx -= 1
By -= 1
S = [list(input()) for i in range(N)]
D = [[[10**7]*N for i in range(N)] for i in range(4)]
dr = [(-1,1), (1,1), (1,-1), (-1,-1)]

if (abs(Ax-Bx)+abs(Ay-By)) % 2 == 1:
    print(-1)
    exit()

q = deque()
for i in range(4):
    D[i][Ax][Ay] = 1
    q.append((Ax, Ay, i, 1))
    
while q:
    x, y, d, cost = q.popleft()
    for i in range(4):
        if D[i][x][y] > cost + 1:
            D[i][x][y] = cost + 1
            q.append((x, y, i, cost + 1))
            
    x += dr[i][0]
    y += dr[i][1]
    if x < 0 or x == N or y < 0 or y == N or S[x][y] == '#':
        continue
    if cost < D[d][x][y]:
        D[d][x][y] = cost
        q.appendleft((x, y, d, cost))

res = 10 ** 7
for i in range(4):
    res = min(res, D[i][Bx][By])
if res != 10 ** 7:
    print(res)
else:
    print(-1)