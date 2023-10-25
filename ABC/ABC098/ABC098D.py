from collections import deque

N = int(input())
A = list(map(int,input().split()))

q = deque()
S = 0
X = 0
ans = 0

for i in A:
    q.append(i)
    S += i
    X = X ^ i
    while S != X:
        a = q.popleft()
        S -= a
        X = X ^ a
    ans += len(q)
    
print(ans)