N = int(input())
S = [list(input()) for i in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == '.':
            continue
        if j + 6 <= N:
            tmp = 0
            for k in range(6):
                if S[i][j+k] == '#':
                    tmp += 1
            if tmp >= 4:
                print('Yes')
                exit()
        if i + 6 <= N:
            tmp = 0
            for k in range(6):
                if S[i+k][j] == '#':
                    tmp += 1
            if tmp >= 4:
                print('Yes')
                exit()
        if i - 5 >= 0 and j + 6 <= N:
            tmp = 0
            for k in range(6):
                if S[i-k][j+k] == '#':
                    tmp += 1
            if tmp >= 4:
                print('Yes')
                exit()
        if i + 6 <= N and j + 6 <= N:
            tmp = 0
            for k in range(6):
                if S[i+k][j+k] == '#':
                    tmp += 1
            if tmp >= 4:
                print('Yes')
                exit()

print('No')