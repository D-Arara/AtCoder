N, X = map(int, input().split())

M = 1001

for i in range(N):
    m = int(input())
    X -= m
    M = min(m, M)

print(N+X//M)