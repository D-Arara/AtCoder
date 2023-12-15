N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

C = set(A)
for b in set(B):
    C.add(b+1)
C = sorted(C)
from bisect import bisect_left, bisect_right
for c in C:
    a = bisect_right(A, c)
    b = M - bisect_left(B, c)
    if a >= b:
        print(c)
        exit()
