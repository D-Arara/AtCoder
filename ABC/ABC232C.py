from itertools import permutations

N, M = map(int, input().split())

a = [[False]*N for i in range(N)]
b = [[False]*N for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    a[A-1][B-1] = a[B-1][A-1] = True

for i in range(M):
    C, D = map(int, input().split())
    b[C-1][D-1] = b[D-1][C-1] = True

for p in permutations(range(N)):
    flag = True
    for i in range(N):
        for j in range(N):
            if a[i][j] != b[p[i]][p[j]]:
                flag = False
    if flag:
        print('Yes')
        exit()

print('No')