from collections import deque

N, K = map(int,input().split())
S = [int(input()) for i in range(N)]

if 0 in S:
    print(N)
    exit()

ans = 0
q = deque()
p = 1

for s in S:
    q.append(s)
    p *= s

    while q and (p > K):
        r = q.popleft()
        p //= r
    
    ans = max(ans, len(q))

print(ans)