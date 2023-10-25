from collections import defaultdict, deque

N, M = map(int, input().split())

nodes = set()
graph = [[] for i in range(N+1)]
INF = 2 * 10 ** 9 + 1 
dist = [INF] * (N+1)

for i in range(M):
    L, R, D = map(int, input().split())
    nodes.add(L)
    nodes.add(R)
    graph[L].append((R,D))
    graph[R].append((L,-D))

def f(nodes):
    for i in nodes:
        if dist[i] < INF:
            continue
        q = deque([i])
        dist[i] = 0
        while q:
            v = q.popleft()
            d = dist[v]
            for to, cost in graph[v]:
                if dist[to] == INF:
                    dist[to] = d + cost
                    q.append(to)
                else:
                    if dist[to] == d + cost:
                        continue
                    else:
                        print('No')
                        exit()

f(nodes)

print('Yes')