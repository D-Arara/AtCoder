from collections import defaultdict
from bisect import bisect_left

N = int(input())

table = list(range(101))
p = 2

while p * p <= 100:
    if table[p] == p:
        for q in range(2*p, 101, p):
            if table[q] == q:
                table[q] = p
    p += 1

D = defaultdict(int)

for i in range(N+1):
    while i > 1:
        D[table[i]] += 1
        i //= table[i] 

L = list(D.values())
L.sort()

index_3 = len(L) - bisect_left(L, 2)
index_5 = len(L) - bisect_left(L, 4)
index_15 = len(L) - bisect_left(L, 14)
index_25 = len(L) - bisect_left(L, 24)
index_75 = len(L) - bisect_left(L, 74)

ans = 0

ans += (index_3 - 2) * index_5 * (index_5 - 1) // 2
ans += (index_5 - 1) * index_15
ans += (index_3 - 1) * index_25
ans += index_75

print(ans)