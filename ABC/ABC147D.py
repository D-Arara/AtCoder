N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

L = [0]*60

for i in A:
    for j in range(60):
        if (i >> j) & 1:
            L[j] += 1

ans = 0

for i in range(60):
    ans += (2 ** i) * L[i] * (N- L[i])
    ans %= mod

print(ans)