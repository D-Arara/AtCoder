from collections import defaultdict
S = list(input())
T = list(input())
U = set(['a', 't', 'c', 'o', 'd', 'e', 'r', '@'])
s = defaultdict(int)
t = defaultdict(int)
a = 0
b = 0
c = defaultdict(int)
d = defaultdict(int)
for i in range(len(S)):
    if not S[i] in U:
        s[S[i]] += 1
    else:
        if S[i] == '@':
            a += 1
        else:
            c[S[i]] += 1
    if not T[i] in U:
        t[T[i]] += 1
    else:
        if T[i] == '@':
            b += 1
        else:
            d[T[i]] += 1
if s == t:
    for i in U:
        if i == '@':
            continue
        a -= max(0, d[i] - c[i])
        b -= max(0, c[i] - d[i])
    if a >= 0 and b >= 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
