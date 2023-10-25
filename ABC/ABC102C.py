N = int(input())
A = list(map(int, input().split()))

m = 0

for i in range(N):
    A[i] -= i + 1

A.sort()

ans = 0
base = A[N//2]

for a in A:
    ans += abs(a - base)

print(ans)