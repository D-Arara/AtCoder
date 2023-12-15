N = int(input())
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        if a:
            a = []
        else:
            a = [2]
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if a and a[-1] == f:
                a.pop()
            else:
                a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        if a and a[-1] == n:
            a.pop()
        else:
            a.append(n)
    return a

from collections import defaultdict
D = defaultdict(int)
for i in range(1,N+1):
    D[tuple(prime_factorize(i))] += 1
res = 0
for v in D.values():
    res += v ** 2
print(res)

