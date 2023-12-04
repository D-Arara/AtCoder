from heapq import heappush, heappop

#s:始点, n:ノード数, gragh:繋がり
def dijkstra(s, n, gragh):
  INF = 10**18
  dist = [INF]*n
  flag = [False]*n
  dist[s] = 0
  q = [(0, s)]  # （距離・ノード）
  while q:
    v = heappop(q)[1]
    if flag[v]:
      continue
    flag[v] = True
    for to, cost in graph[v]:
      if flag[to]:
        continue
      if dist[to] <= dist[v] + cost:
        continue
      dist[to] = dist[v]+ cost
      heappush(q, (dist[to], to))
  return dist

N, M = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))
x = dijkstra(0, N, graph)
y = dijkstra(N-1, N, graph)
for i in range(N):
  print(x[i]+y[i])