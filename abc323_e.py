N, X = map(int, input().split())
T = list(map(int, input().split()))
mod = 998244353

res = [0] * (X+2)
res[0] = 1
N_rev = pow(N, -1, mod)
for i in range(X+1):
    if res[i] == 0:
        continue
    for t in range(N):
        j = T[t]
        if i + j >= X + 1:
            if t == 0:
                res[-1] = (res[-1] + ((N_rev * res[i]) % mod)) % mod
        else:
            res[i+j] = (res[i+j] + ((N_rev * res[i]) % mod)) % mod

print(res[-1])
