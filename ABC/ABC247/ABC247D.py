from bisect import bisect_left
from collections import deque
Q = int(input())
X = deque([])
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        c = q[2]
        X.append((x,c))
    else:
        c = q[1]
        cnt = 0
        res = 0
        while cnt >= c:
            x, d = X.popleft()
            res += x * d
            cnt += d
        if cnt != c:
            tmp = cnt - c
            res -= x * tmp
            X.appendleft((x,tmp))
        print(X)
        print(res)