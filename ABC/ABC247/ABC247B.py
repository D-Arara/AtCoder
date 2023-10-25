N = int(input())
l = []
m = []
for i in range(N):
    s, t = input().split()
    l.append((s,t))
    m.append(s)
    m.append(t)
for i in range(N-1):
    s, t = l[i]
    tmp = set(m[2*(i+1):])
    if not s in tmp or not t in tmp:
        continue
    else:
        print('No')
        exit()
print('Yes')