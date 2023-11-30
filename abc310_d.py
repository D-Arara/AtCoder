N, T, M = map(int, input().split())

from collections import defaultdict
D = defaultdict(set)
for i in range(M):
    A, B = map(int, input().split())
    D[A-1].add(B-1)
    D[B-1].add(A-1)
cnt = 0

S = []
def dfs(n):
    global cnt
    if n == N:
        if len(S) == T:
            cnt += 1
    else:
        if not S:
            S.append(set())
            S[-1].add(n)
            dfs(n+1)
            S.pop()
        else:
            if len(S) < T:
                S.append(set())
                S[-1].add(n)
                dfs(n+1)
                S.pop()
            for i in range(len(S)):
                if not S[i] & D[n]:
                    S[i].add(n)
                    dfs(n+1)
                    S[i].discard(n)
dfs(0)
print(cnt)