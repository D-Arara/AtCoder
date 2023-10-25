S = input()

if S == S[::-1]:
    print('Yes')
    exit()

p = 0

while p < len(S):
    if S[p] == 'a':
        p += 1
    else:
        break

T = S[::-1]

cnt = 0

while cnt < len(T):
    if T[cnt] == 'a':
        cnt += 1
    else:
        break

if p > cnt:
    print('No')
    exit()

S = 'a' * (cnt-p) + S

if S == S[::-1]:
    print('Yes')
else:
    print('No')