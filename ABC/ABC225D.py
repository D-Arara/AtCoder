N, Q = map(int, input().split())

L = [[-1,-1] for i in range(N+1)]

for i in range(Q):
    q = list(map(int, input().split()))
    c = q[0]
    if c == 1:
        x, y = q[1], q[2]
        L[x][1] = y
        L[y][0] = x
    elif c == 2:
        x, y = q[1], q[2]
        L[x][1] = -1
        L[y][0] = -1
    else:
        x = q[1]

        s = L[x][0]
        S = []
        while s != -1:
            S.append(s)
            s = L[s][0]
        
        g = L[x][1]
        G = []
        while g != -1:
            G.append(g)
            g = L[g][1]

        ans = S[::-1] + [x] + G
        print(len(ans), *ans)