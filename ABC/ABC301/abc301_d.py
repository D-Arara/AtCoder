S = list(input())
N = int(input())
m = len(S)
res = 0
for i in range(m):
    if S[i] == '1':
        res += 2 ** (m-1-i)
for i in range(m):
    if S[i] == '?':
        if N >= res + 2 ** (m-1-i):
            res += 2 ** (m-1-i)
if res <= N:
    print(res)
else:
    print(-1)