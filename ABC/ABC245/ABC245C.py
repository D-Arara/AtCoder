N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [A[0], B[0]]
nex = set()
for i in range(N-1):
    for j in dp:
        if abs(j - A[i+1]) <= K:
            nex.add(A[i+1])
        if abs(j - B[i+1]) <= K:
            nex.add(B[i+1])
    if len(nex) == 0:
        print('No')
        exit()
    dp = nex
    nex = set()
print('Yes')