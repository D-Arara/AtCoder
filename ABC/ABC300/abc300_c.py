H, W = map(int, input().split())
C = [(list(input()) + ['.']) for i in range(H)]
C += [['.'] * (W + 1)]

f = [[False] * (W+1) for i in range(H+1)]
cnt = [0] * (min(H, W)+1)

for i in range(H):
    for j in range(W):
        if f[i][j]:
            continue
        for k in range(max(H,W)):
            if C[i+k][j+k] == '#':
                f[i+k][j+k] = True
                continue
            break
        cnt[k//2-1] += 1
print(*cnt[:-1])