from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))

ans = []

def main(L,cnt,ans):
    for i in range(0,n):
        L[i] += cnt
        if L[i-1] * L[i] < 0:
            continue
        if L[i-1] > 0:
            tmp = -1 - L[i]
            L[i] = -1
        else:
            tmp = 1 - L[i]
            L[i] = 1
        cnt += tmp
        ans += abs(tmp)
    return ans

L = list(accumulate(A))
cnt = 0
num = 0

ans.append(main(L+[1],cnt,num))

L = list(accumulate(A))
cnt = 0
num = 0

ans.append(main(L+[-1],cnt,num))

print(min(ans))