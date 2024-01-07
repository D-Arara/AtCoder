N, Q = map(int, input().split())

L = []
for i in range(N):
    L.append([N-i, 0])

D = {'R':(1, 0), 'L':(-1, 0), 'U':(0, 1), 'D':(0, -1)}
for i in range(Q):
    q = list(input().split())
    if q[0] == '1':
        tmp = []
        tmp.append(L[-1][0] + D[q[1]][0])
        tmp.append(L[-1][1] + D[q[1]][1])
        L.append(tmp)
    else:
        print(*L[-int(q[1])])
