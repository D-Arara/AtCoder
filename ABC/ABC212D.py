from heapq import heappush, heappop
Q = int(input())
cnt = 0
L = []

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heappush(L, q[1]-cnt)
    elif q[0] == 2:
        cnt += q[1]
    elif q[0] == 3:
        v = heappop(L)
        print(v+cnt)
