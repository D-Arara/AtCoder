H, W = map(int, input().split())
L = [['.']*(W+2)]

for i in range(H):
    S = list(input())
    L.append(['.'] + S + ['.'])

L.append(['.']*(W+2))

ans = []

for i in range(1,H+1):
    tmp = []
    for j in range(1,W+1):
        if L[i][j] == '#':
            tmp.append('#')
        else:
            cnt = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if k == l == 0:
                        continue
                    if L[i+k][j+l] == '#':
                        cnt += 1
            tmp.append(str(cnt))
    ans.append(tmp)

for i in ans:
    print(*i, sep='')
