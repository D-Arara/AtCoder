N = int(input())
A = list(map(int, input().split()))
res = [A[0]]
for i in range(1,N):
    if A[i-1] < A[i]:
        res += list(range(A[i-1]+1, A[i]+1))
    else:
        res += list(range(A[i-1]-1, A[i]-1, -1))
print(*res)