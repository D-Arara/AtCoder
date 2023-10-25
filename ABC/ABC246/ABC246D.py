N = int(input())
ans = 10**18
for i in range(10**6+1):
    X = i ** 3
    if X >= N:
        a = i
        ans = min(ans, X)
        break
    else:
        continue
for i in range(10**6):
    Y = 4*(i**3)
    if Y >= N:
        b = i
        ans = min(Y, ans)
        break
    else:
        continue
c = 0
d = a
while c != b or d != b:
    print(X)
    if X >= N:
        if d == b:
            break
        ans = min(ans,X)
        d -=1
        X = (c + d) * (c**2 + d**2)
    else:
        if c == b:
            break
        c += 1
        X = (c + d) * (c**2 + d**2)
if X >= N:
        ans = min(ans,X)
print(ans)