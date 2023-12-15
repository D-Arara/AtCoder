N, M = map(int, input().split())
A = list(map(int, input().split()))
AA = [0]
for i in range(N):
    AA.append(AA[-1]+A[i])
res = 0
for i in range(M):
    res += A[i] * (i + 1)
tmp = res
for i in range(N-M):
    tmp = tmp - (AA[M+i]-AA[i]) + A[M+i] * M
    res = max(res, tmp)

print(res)

