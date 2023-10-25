D, G = map(int, input().split())
L = [list(map(int, input().split())) for i in range(D)]

ans = 1001

for i in range(2**D):
    num = 0
    cnt = 0
    tmp = -1
    for j in range(D):
        p, c = L[j]
        if (i >> j) & 1:
            num += p
            cnt += 100 * (j + 1) * p + c
        else:
            tmp = j
    if cnt >= G:
        ans = min(num, ans)
    else:
        p, c = L[tmp]
        for k in range(1,p):
            if cnt + 100 * (tmp + 1) * k >= G:
                ans = min(num+k, ans)
                break

print(ans)