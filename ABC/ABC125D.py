N = int(input())
A = list(map(int, input().split()))

tmp = 10 ** 9 + 1

for i in range(N-1):
    if A[i] < 0:
        A[i] *= -1
        A[i+1] *= -1
    tmp = min(tmp, A[i])

if A[-1] > 0:
    print(sum(A))
else:
    A[-1] *= -1
    tmp = min(tmp, A[-1])
    print(sum(A)-2*tmp)