from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

L = []
for a in A:
    L.append(a)
for b in B:
    L.append(b+1)
L.sort()

for c in L:
    if bisect_right(A, c) >= M - bisect_left(B, c):
        print(c)
        break
