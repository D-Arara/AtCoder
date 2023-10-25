n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

mod = 10 ** 9 + 7

sum_x = 0
sum_y = 0

for i in range(n):
    sum_x += (2 * i - n + 1) * x[i] 
    sum_x %= mod

for i in range(m):
    sum_y += (2 * i - m + 1) * y[i]
    sum_y %= mod

print(sum_x * sum_y % mod)