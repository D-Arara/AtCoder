from itertools import accumulate
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

D = defaultdict(int)
L = accumulate(A)
cnt = 0

for i in L:
    num = i % M
    if num == 0:
        cnt += 1
    else:
        D[num] += 1

ans = 0

def f(x):
    return x * (x+1) // 2

for i in D.values():
    ans += f(i-1)

ans += f(cnt)

print(ans)