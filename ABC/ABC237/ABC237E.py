from heapq import heappush, heappop

#s:始点, n:ノード数, gragh:繋がり
def dijkstra(s, n, gragh):
  INF = 10 ** 18
  dist = [INF]*n
  flag = [False]*n
  dist[s] = - H[0]
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
        dist[to] = dist[v] + cost
        heappush(q, (dist[to], to))
  return dist

N, M = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for i in range(N)]

for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    if H[U] >= H[V]:
        graph[U].append((V, 0))
        graph[V].append((U, H[U] - H[V]))
    else:
        graph[U].append((V, H[V] - H[U]))
        graph[V].append((U, 0))

d = dijkstra(0, N, graph)

for i in range(N):
    d[i] += H[i]

print(-min(d))