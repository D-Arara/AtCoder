N, K = map(int, input().split())
A = list(map(int, input().split()))

a = [0] * 40

for i in A:
    for j in range(40):
        if (i >> j) & 1:
            a[j] += 1

x = [0] * 40
k = 0
ans = 0 

for i in range(39, -1, -1):
    if a[i] < N - a[i] and k + (1 << i) <= K:
        ans += (N - a[i]) * (1 << i)
        k += 1 << i
    else:
        ans += a[i] * (1 << i)

print(ans)