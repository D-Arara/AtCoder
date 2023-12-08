N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    A, B, X, Y = map(int, input().split())
    graph[A-1].append((B-1, X, Y))
    graph[B-1].append((A-1, -X, -Y))

seat = [0] * N
seat[0] = (0, 0)
q = [0]
while q:
    u = q.pop()
    a, b = seat[u]
    for v, x, y in graph[u]:
        if seat[v] != 0:
            continue
        seat[v] = (a+x, b+y)
        q.append(v)

for i in seat:
    if i != 0:
        print(*i)
    else:
        print('undecidable')