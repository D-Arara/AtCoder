from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

S = set()

for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            start = (i, j)
        if A[i][j] == 'G':
            goal = (i, j)
        if A[i][j] == '#':
            S.add((i, j))
        if A[i][j] == '>':
            S.add((i, j))
            for k in range(1,W):
                if j + k >= W or A[i][j+k] != '.':
                    break
                S.add((i, j+k))
        if A[i][j] == 'v':
            S.add((i, j))
            for k in range(1,H):
                if i + k >= H or A[i+k][j] != '.':
                    break
                S.add((i+k, j))
        if A[i][j] == '<':
            S.add((i, j))
            for k in range(1,W):
                if j - k < 0 or A[i][j-k] != '.':
                    break
                S.add((i, j-k))
        if A[i][j] == '^':
            S.add((i, j))
            for k in range(1,W):
                if i - k < 0 or A[i-k][j] != '.':
                    break
                S.add((i-k, j))

visited = [[-1] * W for _ in range(H)]
visited[start[0]][start[1]] = 0

q = deque([start])
dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while q:
    x, y = q.popleft()
    for i, j in dr:
        h, w = x + i, y + j
        if h == -1 or h == H or w == -1 or w == W:
            continue
        if (h, w) in S:
            continue
        if visited[h][w] >= 0:
            continue
        visited[h][w] = visited[x][y] + 1
        q.append((h, w))


    if visited[goal[0]][goal[1]] >= 0:
        print(visited[goal[0]][goal[1]])
        exit()

print(-1)

