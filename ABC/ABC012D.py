class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)] for i in range(N)]  

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
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        hasNegativeCycle = False
        for i in range(self.N):
            if self.d[i][i] < 0:
                hasNegativeCycle = True
                break
        for i in range(self.N):
            self.d[i][i] = 0
        return hasNegativeCycle, self.d

N, M = map(int, input().split())
W = WarshallFloyd(N)

for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    W.add(a,b,t)

h, d = W.WarshallFloyd_search()
ans = float("inf")

for i in range(N):
    ans = min(ans,max(d[i]))

print(ans)