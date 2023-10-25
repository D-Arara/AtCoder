class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)] for i in range(N)]
        self.S = set()

    def add(self, u, v, c, directed=False):
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    if self.d[i][j] == self.d[i][k] + self.d[k][j] and i != k and j != k:
                        self.S.add((i,j))
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
        hasNegativeCycle = False
        for i in range(self.N):
            if self.d[i][i] < 0:
                hasNegativeCycle = True
                break
        for i in range(self.N):
            self.d[i][i] = 0
        return hasNegativeCycle, self.d, self.S
        
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
W = WarshallFloyd(N)

for i in range(N):
    for j in range(N):
        W.add(i,j,A[i][j],True)

h, d, S = W.WarshallFloyd_search()

if A != d:
    print(-1)
else:
    ans = 0
    for i in range(N):
        ans += sum(d[i])
    for i, j in S:
        ans -= A[i][j]
    ans //= 2
    print(ans)