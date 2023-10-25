N, K = map(int, input().split())
tmp = ((N - 2) * (N - 1)) // 2

if K > tmp:
    print(-1)
    exit()

M = N - 1 + tmp - K
print(M)

for i in range(1,N+1):
    for j in range(i+1,N+1):
        print(i, j)
        M -= 1
        if M == 0:
            exit()