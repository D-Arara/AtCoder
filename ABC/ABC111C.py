from collections import Counter

n = int(input())
v = list(map(int, input().split()))

a = v[0::2]
b = v[1::2]

a = Counter(a)
b = Counter(b)

a = a.most_common()
b = b.most_common()

if a[0][0] != b[0][0]:
    print(n - a[0][1] - b[0][1])
else:
    a.append((0,0))
    b.append((0,0))
    tmp_1 = n - a[0][1] - b[1][1]
    tmp_2 = n - a[1][1] - b[0][1]
    print(min(tmp_1,tmp_2))
