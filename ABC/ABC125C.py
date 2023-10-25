from math import gcd

N = int(input())
A = list(map(int, input().split()))
B = A[::-1]

C = [A[0]]
D = [B[0]]

for i in range(N-1):
    C.append(gcd(C[-1], A[i+1]))
    D.append(gcd(D[-1], B[i+1]))

ans = max(C[-2], D[-2])
D = D[::-1]

for i in range(N-2):
    ans = max(ans, gcd(C[i], D[i+2]))

print(ans)