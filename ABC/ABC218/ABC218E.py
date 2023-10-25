from collections import defaultdict
from heapq import heappush, heappop, heapify

class UnionFind():
    def __init__(self, n):
        self.n = n
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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M = map(int, input().split())

U = UnionFind(N)
q = []
heapify(q)
score = 0

for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if C <= 0:
        U.union(A,B)
    else:
        heappush(q, (C, A, B))
        score += C

for i in range(len(q)):
    v = heappop(q)
    if U.same(v[1], v[2]):
        continue
    U.union(v[1], v[2])
    score -= v[0]

print(score)