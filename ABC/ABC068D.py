K = int(input())
N = 50 
ans = []
rem = K % N

for i in range(N-rem):
    ans.append(49-rem)

for i in range(rem):
    ans.append(N)

p = K // N

for i in range(N):
    ans[i] += p

print(N)
print(*ans)