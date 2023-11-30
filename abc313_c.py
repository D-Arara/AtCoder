N = int(input())
A = sorted(list(map(int, input().split())))

cnt = 0
n, m = sum(A)//N, sum(A)%N
for i in range(N):
    if i >= N-m:
        cnt += abs(n+1-A[i])
    else:
        cnt += abs(n-A[i])
print(cnt//2)
