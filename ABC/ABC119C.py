from itertools import product

N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]

ans = 8000
L = [list(range(4)) for i in range(N)]

for i in product(*L):
    cnt = [0] * 4
    tmp = [0] * 4
    num = 0
    for j in range(N):
        cnt[i[j]] += 1
        tmp[i[j]] += l[j]
    if cnt[1] == 0 or cnt[2] == 0 or cnt [3] == 0:
        continue
    if tmp[3] > tmp[2] or tmp[2] > tmp[1]:
        continue
    for j in range(1,4):
        num += 10 * (cnt[j] - 1)
    num += abs(A - tmp[1])
    num += abs(B - tmp[2])
    num += abs(C - tmp[3])
    ans = min(ans, num)

print(ans)