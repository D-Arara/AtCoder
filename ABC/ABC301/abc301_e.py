from collections import deque
H, W, T = map(int, input().split())
A = [list(input()) for _ in range(H)]
O = []
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            s = (i, j)
        if A[i][j] == 'G':
            g = (i, j)
        if A[i][j] == 'o':
            O.append((i, j))

def f(a, b):
    global T
    sx, sy = a
    gx, gy = b
    dx = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque([(sx, sy, 0)])
    S = set()
    S.add((sx, sy))
    while q:
        x, y, d = q.popleft()
        for i, j in dx:
            nx, ny = x + i, y + j
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            if (nx, ny) in S:
                continue
            if A[nx][ny] == '#':
                continue
            if nx == gx and ny ==  gy:
                return d + 1
            if d + 1 == T:
                continue
            S.add((nx, ny))
            q.append((nx, ny, d+1))

so = [-1] * len(O)
og = [-1] * len(O)
for i in range(len(O)):
    so[i] = f(s, O[i])
    og[i] = f(g, O[i])
oo = [[-1] * len(O) for _ in range(len(O))]
for i in range(len(O)-1):
    for j in range(i+1, len(O)):
        tmp = f(O[i], O[j])
        oo[i][j] = tmp
        oo[j][i] = tmp
sg = f(s, g)

if sg > T:
    print(-1)