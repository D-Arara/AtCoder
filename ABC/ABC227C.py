N = int(input())

num = 10**(-7)
ans = 0
tmp = int(N**(1/3))

if int(N**(1/3)) != int(N**(1/3)+tmp):
    tmp += 1

for i in range(1,tmp+1):
    for j in range(i,int((N//i)**(0.5))+1):
        ans += (N // (i*j)) - j + 1

print(ans)