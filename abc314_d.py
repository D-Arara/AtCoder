N = int(input())
S = list(input())
Q = int(input())
tmp = set()
f = 0

for i in range(Q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)
    if t == 1:
        S[x-1] = c
        tmp.add(x-1)
    elif t == 2:
        f = 2
        tmp = set()
    else:
        f = 3
        tmp = set()

if f != 0:
    for i in range(N):
        if i in tmp:
            continue
        if f == 2:
            S[i] = S[i].lower()
        if f == 3:
            S[i] = S[i].upper()
print(*S, sep='')