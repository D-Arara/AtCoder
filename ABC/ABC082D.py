s = input()
x, y = map(int, input().split())

flag = 1
X = []
Y = []
cnt = 0

for i in s:
    if i == 'F':
        cnt += 1
    else:
        if flag == 1:
            X.append(cnt)
        else:
            Y.append(cnt)
        cnt = 0
        flag *= -1

if flag == 1:
    X.append(cnt)
else:
    Y.append(cnt)
        
def f(L,k,p):
    len_L = len(L)
    sum_L = sum(L)
    if sum_L < abs(k):
        return False
    dp = [[False]*(2*(sum_L+1)) for i in range(len_L+1)]
    dp[0][sum_L] = True

    for i in range(len_L):
        for j in range(2*(sum_L+1)):
            if not dp[i][j]:
                continue
            if i == 0 and p == 'x':
                dp[i+1][j+L[i]] = True
            else:
                dp[i+1][j-L[i]] = True
                dp[i+1][j+L[i]] = True
    if dp[len_L][sum_L+k]:
        return True
    else:
        return False

if f(X,x,'x') and f(Y,y,'y'):
    print('Yes')
else:
    print('No')