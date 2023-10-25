T = int(input())
mod = 998244353

for i in range(T):
    N = int(input())
    S = list(map(lambda x: ord(x) - ord('A'), input()))
    ans = 0
    for j in S[:(N+1)//2]:
        ans *= 26
        ans += j
        ans %= mod
    if S[(N-1)//2::-1] <= S[N//2:]:
        ans += 1
        ans %= mod
    print(ans)