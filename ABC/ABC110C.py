from collections import defaultdict

S = input()
T = input()

DS = defaultdict(int)
DT = defaultdict(int)

for i in range(len(S)):
    s = S[i]
    t = T[i]
    if DS[s] != DT[t]:
        print('No')
        exit()
    else:
        DS[s] = i + 1
        DT[t] = i + 1

print('Yes')