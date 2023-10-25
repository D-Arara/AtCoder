N, K, X = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for i in range(N):
    print(A,res)
    s = A[i] // X
    a = A[i] % X
    if s <= K:
        res += a
        A[i] = a
        K -= s
    else:
        print(res+sum(A[i:])-K*X)
        exit()
A.sort(reverse=True)
for i in range(min(K,N)):
    A[i] = 0
print(sum(A))