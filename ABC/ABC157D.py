from collections import defaultdict
import itertools
class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

N, M, K = map(int,input().split())
gf = [set() for i in range(N)]
gb = [set() for i in range(N)]
UF = UnionFind(N)

for i in range(M):
    A, B = map(int,input().split())
    A -= 1
    B -= 1
    gf[A].add(B)
    gf[B].add(A)
    UF.union(A,B)
    
ans = [0]*N
    
for i in range(K):
    C, D = map(int,input().split())
    C -= 1
    D -= 1
    if UF.find(C) == UF.find(D):
        ans[C] -= 1
        ans[D] -= 1

for i in range(N):
    if UF.parents[i] >= 0:
        UF.parents[i] = UF.find(i)

for i in range(N):
    ans[i] += -UF.parents[UF.find(i)] - len(gf[i]) - 1
print(*ans)