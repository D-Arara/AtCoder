N = int(input())
mod = 998244353 
L = len(str(N))

ans = 0

for i in range(1,L):
    tmp = 9 * 10 ** (i - 1)
    ans += (tmp * (tmp + 1)) // 2
    ans %= mod

if L == 1:
    ans += (N * (N + 1)) // 2
else:
    M = N - int('9' * (L - 1))
    ans += (M * (M+1)) // 2
    ans %= mod

print(ans)