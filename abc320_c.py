M = int(input())
S1 = input() * 3
S2 = input() * 3
S3 = input() * 3

inf = 1 << 61
res = inf
for i in range(M*3):
    for j in range(M*3):
        if i == j:
            continue
        for k in range(M*3):
            if i == k or j == k:
                continue
            if S1[i] == S2[j] == S3[k]:
                res = min(res, max(i, j, k))

if res != inf:
    print(res)
else:
    print(-1)
