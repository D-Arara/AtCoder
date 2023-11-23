from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
L = [[] for _ in range(3)]
for i in range(N):
    T, X = map(int, input().split())
    L[T].append(X)
L[0].sort(reverse=True)
L[1].sort()
L[2].sort(reverse=True)

q = L[0][:M]
res = sum(q)
heapify(q)

for i in range(min(len(L[2]), M)):
    tmp = res
    X = L[2][i]
    cnt = M - i
    if len(q) == cnt:
        tmp -= q[0]
        heappop(q)
    while X and L[1]:
        if len(q) < cnt - 1:
            tmp += L[1][-1]
            heappush(q, L[1][-1])
            L[1].pop()
            X -= 1
            res = max(res, tmp)
        else:
            if q[0] >= L[1][-1]:
                print(res)
                exit()
            else:
                tmp -= q[0]
                heappop(q)
                tmp += L[1][-1]
                heappush(q, L[1][-1])
                L[1].pop()
                X -= 1
                res = max(res, tmp)
                
print(res)