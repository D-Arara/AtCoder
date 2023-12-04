def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, 10**6 + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)



print(cmb(80,40,p))

from math import factorial
def nCr(n,r):
    return factorial(n) // (factorial(n-r) * factorial(r))
print(nCr(80,40))