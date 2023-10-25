A, B, C, D, E, F = map(int, input().split())

num = F // 100
ans = 0
ab = [A*100,0]

for i in range(num//A+1):
    for j in range((num-A*i)//B+1):
        if i == j == 0:
            continue
        cnt = E * (A*i + B*j)
        for k in range(cnt//C+1):
            for l in range((cnt-C*k)//D+1):
                a = (A*i + B*j) * 100 
                b = C*k + D*l
                if b/(a+b) > ans and a+b <= F:
                    ans = b/(a+b) 
                    ab = [a+b, b]

print(*ab)
