from math import factorial

N, K = map(int, input().split())
mod = 10 ** 9 + 7

def nCr(n,r):
    return factorial(n) // (factorial(r) * factorial(n - r))

for i in range(1,K+1):
    if N - K + 1 < i:
        print(0)
    else:
        print(nCr(K-1, i-1) * nCr(N-K+1, i) % mod)