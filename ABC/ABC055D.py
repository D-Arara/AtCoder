N = int(input())
s = input()

tmp = [['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W']]

for L in tmp:
    for i in range(1,N):
        if s[i] == 'o':
            if L[-1] == 'S':
                L.append(L[-2])
            else:
                if L[-2] == 'S':
                    L.append('W')
                else:
                    L.append('S')
        else:
            if L[-1] == 'S':
                if L[-2] == 'S':
                    L.append('W')
                else:
                    L.append('S')
            else:
                L.append(L[-2])
    if s[0] == 'o':
        if L[0] == 'S':
            L = [L[1]] + L
        else:
            if L[1] == 'S':
                L = ['W'] + L
            else:
                L = ['S'] + L
    else:
        if L[0] == 'S':
            if L[1] == 'S':
                L = ['W'] + L
            else:
                L = ['S'] + L
        else:
            L = [L[1]] + L

    if L[0:2] == L[N:]:
        print(*L[1:N+1], sep='')
        exit()

print(-1)