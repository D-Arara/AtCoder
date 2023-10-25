N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

ans = 0

for i in range(N):
    tmp = sum(A[0][:i+1]) + sum(A[1][i:])
    ans = max(tmp, ans)

print(ans)