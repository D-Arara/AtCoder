from collections import deque

N, K = map(int, input().split())
mod = 10 ** 9 + 7

graph = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

flag = [False] * N
ans = K
flag[0] = True
q = deque([0])

while q:
    v = q.popleft()
    if v == 0:
        cnt = -1
    else:
        cnt = 0
    for i in graph[v]:
        if flag[i]:
            continue
        ans *= K - 2 - cnt
        ans %= mod
        cnt += 1
        q.append(i)
        flag[i] = True

print(ans)