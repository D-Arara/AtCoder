N, K = map(int, input().split())
L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append(B)
    L.append(A-B)
L.sort(reverse=True)
print(sum(L[:K]))