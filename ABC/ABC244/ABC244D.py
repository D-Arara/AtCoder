S = list(input())
T = list(input())

if S == T:
    print('Yes')
elif T == [S[1], S[2], S[0]]:
    print('Yes')
elif T == [S[2], S[0], S[1]]:
    print('Yes')
else:
    print('No')