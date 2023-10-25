N, M = map(int, input().split())

L = [list(map(int, input().split())) for i in range(N)]

ans = []

for i in range(2**3):
    flag = [1]*3
    for j in range(3):
        if (i >> j) & 1:
            flag[j] *= -1
    tmp = []
    for l in L:
        cnt = 0
        for k in range(3):
            cnt += l[k] * flag[k]
        tmp.append(cnt)
    tmp.sort(reverse=True)
    ans.append(sum(tmp[:M]))

print(max(ans))