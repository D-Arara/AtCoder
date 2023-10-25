N = int(input())

R = [(list(map(int, input().split())) + [0,False]) for i in range(N)]
B = [(list(map(int, input().split())) + [1,False]) for i in range(N)]

L = R + B

L.sort()

ans = 0

for i in range(2*N):
    if L[i][2] == 0 or L[i][3]:
        continue
    tmp = []
    for j in range(i):
        if L[j][2] == 1 or L[j][3]:
            continue
        if L[i][1] > L[j][1]:
            tmp.append((L[j][1],j))
    if len(tmp) == 0:
        continue
    tmp.sort()
    L[tmp[-1][1]][3] = True
    ans += 1

print(ans)