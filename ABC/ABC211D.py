from collections import deque

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

q = deque([1])
dist = [-1] * (N+1)
route = [0] * (N+1)
dist[1] = 0
route[1] = 1

ans = 0
mod = 10 ** 9 + 7

while q:
    v = q.popleft()
    d = dist[v]
    for to in graph[v]:
        if dist[to] == d + 1:
            route[to] += route[v]
            route[to] %= mod
        if dist[to] == -1:
            dist[to] = d + 1
            route[to] += route[v]
            q.append(to)
        
print(route[N])