#abc192E
from heapq import heappop, heappush
def dijkstra(s,n,graph):
  INF = 10**18
  dist = [INF]*n
  dist[s] = 0
  q = [(0,s)]
  flag = [False]*n
  while q:
    v = heappop(q)[1]
    if flag[v]:
      continue
    flag[v] = True
    for to, cost, k in graph[v]:
      if flag[to]:
        continue
      d = (-(-dist[v] // k) * k) + cost
      if dist[to] <= d:
        continue
      dist[to] = d
      heappush(q, (dist[to], to))

  return dist

N, M, X, Y = map(int,input().split())
X -= 1
Y -= 1
graph = [[] for i in range(N)]
for i in range(M):
  A, B, T, K = map(int,input().split())
  A -= 1
  B -= 1
  graph[A].append((B, T, K))
  graph[B].append((A, T, K))
ans = dijkstra(X, N, graph)[Y]
print(ans) if ans != 10**18 else print(-1)