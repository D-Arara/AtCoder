N = int(input())

def read():
    S = set()
    for y in  range(N):
        s = input()
        for x in range(N):
            if s[x] == '#':
                S.add((x,y))
    return S

S = read()
T = read()

for i in range(4):
    mx, my = min(S)
    S = set((x-mx, y-my) for x, y in S)
    mx, my = min(T)
    T = set((x-mx, y-my) for x, y in T)

    if S == T:
        print('Yes')
        exit()

    T = set((y, -x) for x, y in T)

print('No')