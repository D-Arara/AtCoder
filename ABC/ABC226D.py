from fractions import Fraction

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
L.sort()

ans = set()

for i in range(N):
    for j in range(i+1,N):
        x = L[i][0] - L[j][0]
        y = L[i][1] - L[j][1]
        if y == 0:
            ans.add('0')
        else:
            tmp = Fraction(x,y)
            ans.add(tmp)

print(len(ans)*2)