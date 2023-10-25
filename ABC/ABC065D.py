from collections import defaultdict

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

N = int(input())

U= UnionFind(N)

nodes = []

for i in range(N):
    x, y = map(int, input().split())
    nodes.append((i, x, y))

X = sorted(nodes, key=lambda x: x[1])
Y = sorted(nodes, key=lambda y: y[2])

edges = []

for i in range(N-1):
    edges.append((X[i+1][1] - X[i][1], X[i][0], X[i+1][0]))
    edges.append((Y[i+1][2] - Y[i][2], Y[i][0], Y[i+1][0]))

edges.sort()

ans = 0

for cost, x, y in edges:
    if U.same(x, y):
        continue
    U.union(x, y)
    ans += cost

print(ans)