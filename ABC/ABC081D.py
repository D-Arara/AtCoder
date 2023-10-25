N = int(input())
a = list(map(int, input().split()))

m = min(a)
M = max(a)

ans = []
cnt = 0

if M >= -m:
    num = a.index(M)
    for i in range(N):
        if a[i] < 0:
            a[i] += M
            ans.append((num+1,i+1))
            cnt += 1
    a[0] += M
    ans.append((num+1,1))
    print(cnt+N)
    for i in ans:
        print(*i)
    for i in range(1,N):
        print(i, i+1)
    
else:
    num = a.index(m)
    for i in range(N):
        if a[i] > 0:
            a[i] += m
            ans.append((num+1,i+1))
            cnt += 1
    a[-1] += m
    ans.append((num+1,N))
    print(cnt+N)
    for i in ans:
        print(*i)
    for i in range(N,1,-1):
        print(i, i-1)

#自力AC文句なし