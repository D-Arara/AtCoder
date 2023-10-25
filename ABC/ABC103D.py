N, M = map(int, input().split())

L = [list(map(int, input().split())) for i in range(M)]

L = sorted(L,key=lambda x: x[1])

ans = 0
now = 0

for s, g in L:
    if s >= now:
        now = g
        ans += 1

print(ans)