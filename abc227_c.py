N = int(input())

res = 0
tmp = int(N**(1/3)) + 1

for i in range(1,tmp+1):
    for j in range(i,int((N//i)**(0.5))+1):
        res += (N // (i*j)) - j + 1

print(res)
