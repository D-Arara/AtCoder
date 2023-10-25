from collections import defaultdict
import itertools
N = int(input())

D = defaultdict(list)

for i in range(N):
    x, y = map(int, input().split())
    D[x].append(y)

L = []

for i in D.values():
    L.append(list((itertools.combinations(sorted(i), 2))))

ans = 0

for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        ans += len(set(L[i]) & set(L[j]))

print(ans)