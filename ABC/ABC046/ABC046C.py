N = int(input())
T, A = map(int,input().split())
for i in range(1,N):
    t, a = map(int,input().split())
    m = -(-T//t)
    n = -(-A//a)
    s = max(m,n)
    T *= s
    A *= s
print(T+A)