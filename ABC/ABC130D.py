from itertools import accumulate
from bisect import bisect_left

N, K = map(int, input().split())
a = list(map(int, input().split()))

A = [0] + list(accumulate(a))
ans = 0

for i in range(1, N+1):
    ans += N - bisect_left(A, A[i - 1] + K) + 1

print(ans)