from heapq import heappush, heappop, heapify

N, K = map(int, input().split())
P = list(map(int, input().split()))

q = heapify(P[:K])
ans = heappop(q)
print(ans)

for i in range(K,N):
    if P[i] < ans:
        print(ans)
    else:
        heappush(q, P[i])
        ans = heappop(q)
        print(ans)
