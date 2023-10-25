N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
INF = 10 ** 6

def my_index(l, x, default=False):
    if x in set(l):
        return l.index(x)
    else:
        return default

P = []
a = my_index(A, X, INF)
b = my_index(A, Y, INF)
if a == INF or b == INF:
    print(0)
    exit()
P.append(min(a,b))
if a < b:
    flag = True
else:
    flag = False

for i in range(N):
    if A[i] == X and not flag:
        P.append(i)
        flag = True
    if A[i] == Y and flag:
        P.append(i)
        flag = False

M = len(P)
P += [N, -1]
res = 0
for i in range(M-1):
    l = P[i]
    r = P[i+1]
    if min(A[l:r+1]) != Y or max(A[l:r+1]) != X:
        break
    cnt_l = 1
    cnt_r = 1
    for j in range(l-1, P[i-1], -1):
        if Y <= j <= X:
            cnt_l += 1
        else:
            break
    for j in range(r+1, P[i+2], -1):
        if Y <= j <= X:
            cnt_r += 1
        else:
            break
    print(cnt_l,cnt_r)
    res += cnt_l * cnt_r
    
print(res)