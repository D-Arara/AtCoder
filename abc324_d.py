from collections import defaultdict, Counter
N = int(input())
S = list(map(int, input()))

res = [0] * 10
res_zero = 0
for i in S:
    res[i] += 1

cnt = 0
i = 0
while i ** 2 <= 10 ** N - 1:
    T = list(map(int, str(i**2)))
    tmp = [0] * 10
    for j in T:
        tmp[j] += 1
    if tmp[1:] == res[1:]:
        cnt += 1
    i += 1
print(cnt)
