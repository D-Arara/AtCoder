N = int(input())

from collections import defaultdict
H = set()
W = set()
D = set()
Box = []
for i in range(N):
    h, w, d = sorted(map(int, input().split()))
    H.add(h)
    W.add(w)
    D.add(d)
    Box.append((h, w, d))

Box.sort()
H = sorted(H)
H = dict(zip(H, range(len(H))))
W = sorted(W)
W = dict(zip(W, range(len(W))))
D = sorted(D)
D = dict(zip(D, range(len(D))))
for i in range(N):
    Box[i] = (H[Box[i][0]], W[Box[i][1]], D[Box[i][2]])

DD = defaultdict(int)
for i in range(N):
    DD[Box[i][1]] = max(DD[Box[i][1]], Box[i][2])
# print(Box)
# print(DD)
for i in range(N):
    w = Box[i][1]
    d = Box[i][2]
    for j in range(w+1,len(W)):
        # print(i, j)
        if d < DD[j]:
            print('Yes')
            exit()
print('No')