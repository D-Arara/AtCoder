N = int(input())
A = list(map(int, input().split()))

A = sorted(list(set(A))) + [0]
for i in range(len(A)):
    if A[i] != i:
        print(i)
        exit()
        