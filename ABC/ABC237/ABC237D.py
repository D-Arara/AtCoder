from collections import deque

N = int(input())
S = input()
S = S[::-1]

ans = deque([N])

for i in range(N):
    if S[i] == 'R':
        ans.appendleft(N-i-1)
    else:
        ans.append(N-i-1)

print(*ans)
