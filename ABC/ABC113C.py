N, M = map(int, input().split())
L = []
for i in range(M):
    p, y = map(int, input().split())
    L.append((p, y, i))

ans = ['']*M
L.sort()

tmp = 0
cnt = 1

for p, y, i in L:
    if tmp == p:
        cnt += 1
    else:
        tmp = p
        cnt = 1
    ans[i] = '0' * (6 - len(str(p))) + str(p) + '0' * (6 - len(str(cnt))) + str(cnt)

for i in ans:
    print(i)