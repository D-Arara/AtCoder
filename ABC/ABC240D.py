N = int(input())
a = list(map(int, input().split()))

b = list()
num = list()

ans = 0
cnt = 0
tmp = 0

for i in range(N):
    if tmp == 0:
        cnt = 1
        b.append(a[i])
        tmp += 1
        print(tmp)
        

    elif b[-1] == a[i]:
        tmp += 1
        cnt += 1
        if cnt == a[i]:
            b.pop()
            tmp -= cnt
            if len(num) == 0:
                cnt = 0
            else:
                cnt = num.pop()
        print(tmp)
        
    else:
        num.append(cnt)
        b.append(a[i])
        tmp += 1
        cnt = 1
        print(tmp)