from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)

N = int(input())
C = list(map(int, input().split()))
C = [0] + C

graph = [[] for i in range(N+1)]

for i in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

d = defaultdict(int)
ans = []

def dfs(v,p):
    if d[C[v]] == 0:
        ans.append(v)
    d[C[v]] += 1
    for to in graph[v]:
        if to == p:
            continue
        dfs(to,v)
        d[C[to]] -= 1

dfs(1,0)

ans.sort()
        
for i in ans:
    print(i)