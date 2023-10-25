H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

L_W = [[] for i in range(H)]
L_H = [[] for i in range(W)]

for i in range(H):
    cnt = 0
    for j in range(W):
        if S[i][j] == '#':
            L_W[i] += [cnt] * cnt
            L_W[i] += [0]
            cnt = 0
        else:
            cnt += 1
    L_W[i] += [cnt] * cnt
            

for j in range(W):
    cnt = 0
    for i in range(H):
        if S[i][j] == '#':
            L_H[j] += [cnt] * cnt
            L_H[j] += [0]
            cnt = 0
        else:
            cnt += 1    
    L_H[j] += [cnt] * cnt
        
ans = 0

for i in range(H):
    for j in range(W):
        ans = max(ans, L_W[i][j]+L_H[j][1]-1)

print(ans)