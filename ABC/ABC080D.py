from random import randrange


N, C = map(int, input().split())

T = [[0] * 10 ** 5 + 1 for i in range(C)]

for i in range(N):
    s, t, c = map(int, input().split())
    T[c-1][s-1] += 1
    T[c-1][t] -= 1

for i in range(10**5):
    for c in range(C):
        T[c][i+1] += T[c][i]

for i in range(10**5):
    for c in range(C):
        if T[c][i]:
            T[c][i] = 1

ans = 0

for i in range(10**5+1):
    tmp = 0
    for c in range(C):
        tmp += T[c][i]
    ans = max(ans, tmp)

print(ans)