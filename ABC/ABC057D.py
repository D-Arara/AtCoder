from math import factorial

def nCr(n,r):
    return factorial(n) // (factorial(n-r) * factorial(r))

N, A, B = map(int ,input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)

if V[A-1] != V[A]:
    print(sum(V[:A])/A)
    print(1)
else:
    num = V.index(V[A])
    cnt = V.count(V[A])
    m = A - num
    M = min(cnt,B-num)
    ans = 0
    if V[0] == V[A]:
        for i in range(m,M+1):
            ans += nCr(cnt,i)
    else:
        ans += nCr(cnt,m)
    print(sum(V[:A])/A)
    print(ans)