N, K = map(int, input().split())

L = [tuple(map(int, input().split())) for i in range(N)]

X = sorted(L, key=lambda x: x[0])
Y = sorted(L, key=lambda y: y[1])

ans = 4 * 10 ** 18 + 1

for i in range(N-1):
    for j in range(N-1):
        for k in  range(i+1,N):
            for l in range(j+1,N):
                x0 = X[i][0]
                x1 = X[k][0]
                y0 = Y[j][1]
                y1 = Y[l][1]
                cnt = 0
                for m in range(N):
                    if x0 <= L[m][0] <= x1 and y0 <= L[m][1] <= y1:
                        cnt += 1
                if cnt >= K:
                    ans = min(ans, (x1 - x0) * (y1 - y0))

print(ans)