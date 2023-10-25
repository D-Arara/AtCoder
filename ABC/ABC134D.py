def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N = int(input())
a = list(map(int, input().split()))

D = [[] for i in range(N)]
for i in range(N):
    D[i].append(make_divisors(i+1))

ans = [0] * N
L = []
for i in range(N-1,-1,-1):
    if ans[i] == a[i]:
        continue
    L.append(i+1)
    for j in D[i]:
        ans[j] ^= 1
        
print(len(L))
print(*L)