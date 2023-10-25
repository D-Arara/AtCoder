N = int(input())
l = []
r = []
for i in range(N):
    tmp = l + [i+1] + r
    l = tmp
    r = tmp
print(tmp)