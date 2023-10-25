def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table

N = int(input())
f, t = sieve(int((N/12)**0.5)+1)
cnt = 0

for i in range(len(t)-2):
    if t[i] ** 2 > N:
        break
    for j in range(i+1,len(t)-1):
        if t[i] ** 2 * t[j] > N:
            break
        for k in range(j+1,len(t)):
            if t[i] ** 2 * t[j] * t[k] ** 2 > N:
                break
            cnt += 1
print(cnt)