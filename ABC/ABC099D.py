N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]

cost = [[0]*3 for i in range(C)]

for i in range(C):
    for j in range(N):
        for k in range(N):
            cost[i][(j+k)%3] += D[c[j][k]-1][i]

ans = 10 ** 9

for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or k == i:
                continue
            tmp = cost[i][0] + cost[j][1] + cost[k][2]
            ans = min(ans, tmp)

print(ans)