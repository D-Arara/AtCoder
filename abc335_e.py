import sys
sys.setrecursionlimit(10**8)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

def dfs(u):
    global res
    for v in graph[u]:
        if v in S:
            continue
        if L[-1] > A[v]:
            continue
        S.add(v)
        L.append(A[v])
        if v == N - 1:
            res = max(res, len(set(L)))
        else:
            dfs(v)
        S.discard(v)
        L.pop()

res = 0
S = set([0])
L = [A[0]]
dfs(0)
print(res)
