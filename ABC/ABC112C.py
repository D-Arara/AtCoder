N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
L = sorted(L, key=lambda x:x[2], reverse=True)

for i in range(101):
    for j in range(101):
        h = abs(i - L[0][0]) + abs(j - L[0][1]) + L[0][2]
        for k in L[1:]:
            if k[2] == 0:
                if abs(i - k[0]) + abs(j - k[1]) < h:
                    break
            else:
                if abs(i - k[0]) + abs(j - k[1]) + k[2] != h:
                    break
        else:
            print(i, j, h)