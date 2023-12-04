N = int(input())
mod = 10 ** 9 + 7
res = 0
for i in range(N):
    res *= sum(list(map(int, input().split())))
    res %= mod