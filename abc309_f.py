N = int(input())

from collections import defaultdict
H = defaultdict(list)
W = defaultdict(int)
D = defaultdict(int)
Box = []
for i in range(N):
    h, w, d = map(int, input().split())
    H[h].append((w, d))
    W[w] += 1
    D[d] += 1
    Box.append((h, w, d))
    
Box.sort()
w = max(W.keys())
d = max(D.keys())
for i in sorted(H.keys()):
    print(i)

