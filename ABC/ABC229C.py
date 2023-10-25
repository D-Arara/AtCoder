from collections import deque

S = input()
K = int(input())

q = deque()

for i in range(len(S)):
    if S[i] == '.':
        q.append(i)
        if len(q) == K+1:
            break
else:
    print(len(S))
    exit()

ans = q[-1]

for j in range(i+1,len(S)):
    if S[j] == '.':
        q.append(j)
        r = q.popleft()
        ans = max(ans,j-r-1)

r = q.popleft()
print(max(ans,len(S)-r-1))