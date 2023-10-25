s = input()
K = int(input())
l = sorted(list(set(s)))
ans = []
cnt = 0

while len(ans) < K:
    L = [i for i, x in enumerate(list(s)) if x == l[cnt]]
    tmp = []
    for i in L:
        if i + K <= len(s) :
            tmp.append(s[i:i+K])
        else:
            tmp.append(s[i:])
    tmp.sort()
    for i in range(len(L)):
        for j in range(len(tmp[i])):
            ans.append(tmp[i][:j+1])
    ans = sorted(list(set(ans)))
    cnt += 1

print(ans[K-1])
