N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]

ans = []

for i in range(M+1):
    tmp = C[i] // A[0]
    ans.append(tmp)
    for j in range(N+1):
        C[i+j] -= tmp * A[j]
        
print(*ans)