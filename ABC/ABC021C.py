from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for i in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

INF = 101
MOD = 10 ** 9 + 7

dist = [INF]*(N+1)
dp = [0]*(N+1)

dist[a] = 0
dp[a] = 1

q = deque([a])

while q:
    v = q.popleft()
    for to in graph[v]:
        if dist[to] == dist[v] + 1:
            dp[to] += dp[v]
            dp[to] %= MOD

        if dist[to] == INF:
            dist[to] = dist[v] + 1
            dp[to] += dp[v]
            dp[to] %= MOD
            q.append(to)

print(dp[b])