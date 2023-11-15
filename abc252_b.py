N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = max(A)
for b in B:
    if A[b-1] == a:
        print('Yes')
        exit()
print('No')