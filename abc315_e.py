N = int(input())
B = [[]] + [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N+1)]

L = [0] * (N+1)
<<<<<<< HEAD
=======
res = set()
>>>>>>> c7c4924a70d22b2a5a76979aba9b29d15aaf7a91
for i in range(1,N+1):
    L[i] = B[i][0]
    if L[i] != 0:
        for j in B[i][1:]:
            graph[j].append(i)

q = [1]
<<<<<<< HEAD
res = set()
=======
>>>>>>> c7c4924a70d22b2a5a76979aba9b29d15aaf7a91
visited = set([1])
while q:
    u = q.pop()
    for v in B[u][1:]:
        if v in visited:
            continue
        visited.add(v)
        if B[v][0] == 0:
            res.add(v)
        else:
            q.append(v)
            
q = list(res)
res = list(res)
while q:
    u = q.pop()
    for v in graph[u]:
        L[v] -= 1
<<<<<<< HEAD
        if L[v] == 0:
=======
        if L[v] == 0 and v in visited:
>>>>>>> c7c4924a70d22b2a5a76979aba9b29d15aaf7a91
            q.append(v)
            res.append(v)
            
print(*res[:-1])
