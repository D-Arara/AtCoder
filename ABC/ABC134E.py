from bisect import bisect_right, bisect_left

N = int(input())
A = [int(input()) for i in range(N)]

INF = 10 ** 9 + 1
A = A[::-1]
L = [INF]*N


for i in A:
    index = bisect_right(L, i)
    L[index] = i

index = bisect_left(L,INF)

print(index)