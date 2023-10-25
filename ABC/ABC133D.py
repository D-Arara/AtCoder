N = int(input())
A = list(map(int, input().split()))

ans = []
tmp = 0

for i in range(N):
    if i % 2 == 0:
        tmp += A[i]
    else:
        tmp -= A[i]

ans.append(tmp)

for i in range(N-1):
    ans.append((A[i] - ans[-1]//2) * 2)

print(*ans)