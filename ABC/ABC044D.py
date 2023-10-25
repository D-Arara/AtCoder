n = int(input())
s = int(input())

def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + n % b

if s > n:
    print(-1)
    exit()

if s == n:
    print(n+1)
    exit()

for b in range(2, int(n**0.5)+1):
    if f(b, n) == s:
        print(b)
        exit()

for i in range(int(n**0.5),0,-1):
    if (n - s) % i == 0:
        b = (n - s) // i + 1
        if f(b, n) == s:
            print(b)
            exit()

print(-1)