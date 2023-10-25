N, K = map(int,input().split())
ans = 0
if K == 0:
  print(N*N)
  exit()
for i in range(N-K):
    b = K + 1 + i
    tmp = (N-b+1) // b
    ans += (i+1) * (tmp+1)
    if (N-K) // b != tmp:
        ans += N - (b*(tmp+1)) - K + 1
print(ans)