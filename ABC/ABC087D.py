from collections import defaultdict, deque

N, M = map(int, input().split())

L_nodes = set()
R_nodes = set()
graph = defaultdict(list)
dist = defaultdict(int)

for i in range(M):
    L, R, D = map(int, input().split())
    L_nodes.add(L)
    R_nodes.add(R)
    graph[L].append((R,D))
    dist[L] = -1
    dist[R] = -1

def f(nodes):
    for i in nodes:
        q = deque([i])
        if dist[i] < 0:
            dist[i] = 0
        while q:
            v = q.popleft()
            d = dist[v]
            for to, cost in graph[v]:
                if dist[to] < 0:
                    dist[to] = d + cost
                    q.append(to)
                else:
                    if dist[to] == d + cost:
                        continue
                    else:
                        print('No')
                        exit()

f(L_nodes-R_nodes)
f(L_nodes|R_nodes)

print('Yes')

# 自力AC汚いけど矛盾判定
