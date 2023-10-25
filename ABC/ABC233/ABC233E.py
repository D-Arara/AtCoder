from itertools import accumulate

X = input()

L = [int(i) for i in X]
A = list(accumulate(L))[::-1]

ans = []
m = 0

for i in A:
    m += i
    ans.append(m%10)
    m //= 10

while m > 0:
    ans.append(m%10)
    m //= 10

print(*ans[::-1], sep='')