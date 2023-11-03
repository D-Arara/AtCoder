H, W, N = map(int, input().split())

L = [[0] * W for _ in range(H)]
hole = []
for i in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    hole.append((a, b))
    L[a][b] = 1

res = -len(hole)
for i in range(min(H,W)):
    res += (H-i) * (W-i)

for a, b in hole:
    d = min(a, b)
    for i in range(1,d+1):
        tmp = 1
        tmp += L[a-i][b-i]
        tmp += L[a][b-i]
        tmp += L[a-1][b]
        res -= 1/tmp
    
    d = min(a, W-1-b)
    tmp = 1
    for i in range(1,d+1):
        tmp = 1
        tmp += L[a-i][b+i]
        tmp += L[a][b+i]
        tmp += L[a-1][b]
        res -= 1/tmp
    
    d = min(H-1-a, b)
    for i in range(1,d+1):
        tmp = 1
        tmp += L[a+i][b-i]
        tmp += L[a][b-i]
        tmp += L[a+1][b]
        res -= 1/tmp
    
    d = min(H-1-a, W-1-b)
    for i in range(1,d+1):
        tmp = 1
        tmp += L[a+i][b+i]
        tmp += L[a][b+i]
        tmp += L[a+1][b]
        res -= 1/tmp
    
    
print(int(res))