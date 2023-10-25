from collections import deque

N = int(input())

graph = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

d_1 = [-1] * (N+1)
d_n = [-1] * (N+1)

def f(x, d):
    q = deque([x])
    d[x] = 0
    while q:
        v = q.popleft()
        for to in graph[v]:
            if d[to] >= 0:
                continue
            d[to] = d[v] + 1
            q.append(to)

f(1, d_1)
f(N, d_n)

cnt_1 = 0
cnt_n = 0

for i in range(1,N+1):
    if d_1[i] <= d_n[i]:
        cnt_1 += 1
    else:
        cnt_n += 1
if cnt_1 > cnt_n:
    print('Fennec')
else:
    print('Snuke')

#解法だけみて実装は自力