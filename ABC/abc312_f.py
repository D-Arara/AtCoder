from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
L = [[] for _ in range(3)]
for i in range(N):
    T, X = map(int, input().split())
    L[T].append(X)
for i in range(3):
    L[i].sort(reverse=True)

q = L[0][:M]
res = sum(q)
heapify(q)


for i in range(L[2]):
    