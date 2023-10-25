def power(a, b, p):
    if b == 0:
        return(1)
    if b % 2 == 0:
        d = power(a, b//2, p)
        return d * d % p
    if b % 2 == 1:
        return (a * power(a, b-1, p)) % p

H, W, A, B = map(int,input().split())
p = 10 **9 + 7
ans = 0

X = [1] * (W+H-1)

for i in range(1,H+W-1):
    X[i] = (X[i-1] * i % p)

Y = [1] * (H+W-1)
Y[H+W-2] = power(X[H+W-2], p-2, p)

for i in range(H+W-3, -1, -1):
    Y[i] = Y[i+1] * (i+1) % p

for h in range(H-A):
    ans += X[B+h-1] * Y[h] * Y[B-1] * X[H+W-B-h-2] *Y[H-h-1] * Y[W-B-1] % p

print(ans)