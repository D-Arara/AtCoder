from itertools import accumulate

N, M, Q = map(int, input().split())

cnt = [[0]*501 for i in range(501)]

for i in range(M):
    L, R = map(int, input().split())
    cnt[L][R] += 1

ans = []

for i in cnt:
    ans.append(list(accumulate(i)))

for i in range(Q):
    p, q = map(int, input().split())
    cnt = 0
    for j in range(p,q+1):
        cnt += ans[j][q]
    print(cnt)