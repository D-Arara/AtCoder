from itertools import combinations
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for a, b, c, d, e in combinations(A, 5):
    if a % P * b % P * c % P * d % P * e % P == Q:
        res += 1
        
print(res)
