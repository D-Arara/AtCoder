N, K = map(int, input().split())
mod = 10 ** 5
visited = [False] * (mod + 1)

def f(n):
    cnt = 0 
    while n > 0:
        cnt += n % 10
        n //= 10
    return cnt

L = []
N = (N + f(N)) % mod
while not visited[N] and len(L) < K:
    visited[N] = True
    L.append(N)
    N = (N + f(N)) % mod
    
if len(L) == K:
    print(L[-1])
else:
    tmp = L.index(N)
    K -= tmp + 1
    l = len(L)
    K %= l - tmp
    K += tmp
    print(L[K])
