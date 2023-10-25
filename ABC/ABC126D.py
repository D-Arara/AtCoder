from collections import deque

N = int(input())
graph = [[] for i in range(N)]

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

ans = [-1] * N
q = deque([0])
ans[0] = 0

while q:
    s = q.popleft()
    for to, d in graph[s]:
        if ans[to] != -1:
            continue
        if d % 2 == 0:
            if ans[s] == 0:
                ans[to] = 0
            else:
                ans[to] = 1
            
        else:
            if ans[s] == 0:
                ans[to] = 1
            else:
                ans[to] = 0
        q.append(to)
            

for a in ans:
    print(a)