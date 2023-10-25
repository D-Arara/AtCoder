from collections import deque

N = int(input())
A = list(map(int, input().split()))

q = deque([A[0]])
ans = 0

for i in range(1,N):
    if A[i] > A[i-1]:
        q.append(A[i])
    else:
        ans += ((len(q)+1) * len(q)) // 2
        q = ([A[i]])

ans += ((len(q)+1) * len(q)) // 2
print(ans)