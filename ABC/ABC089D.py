from collections import defaultdict
from itertools import accumulate

H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

T = defaultdict(tuple)

for i in range(H):
    for j in range(W):
        T[A[i][j]] = (i+1, j+1)

cnt = []

for i in range(D):
    tmp = []
    for j in range(i+1,H*W+1-D,D):
        tmp.append(abs(T[j+D][0] - T[j][0]) + abs(T[j+D][1] - T[j][1]))
    cnt.append(list(accumulate(tmp))+[0])

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split())
    rem = L % D
    if rem == 0:
        print(cnt[rem-1][R//D - 2] - cnt[rem-1][L//D - 2])
    else:
        print(cnt[rem-1][(R-rem)//D-1] - cnt[rem-1][(L-rem)//D-1])