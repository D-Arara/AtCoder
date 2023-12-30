N, T = input().split()

front = [0] * (len(T)+1)
back = [0] * (len(T)+1)
for i in range(int(N)):
    S = input()
    t = 0
    for j in range(len(S)):
        if T[t] == S[j]:
            t += 1
            if t == len(T):
                break
    front[t] += 1
    t = 0
    for j in range(len(S)-1,-1,-1):
        if T[len(T)-t-1] == S[j]:
            t += 1
            if t == len(T):
                break
    back[t] += 1

from itertools import accumulate
front = list(accumulate(front[::-1]))
# back = list(accumulate(back[::-1]))
back = back[::-1]
res = 0
for i in range(len(T)+1):
    res += front[i] * back[len(T)-i]
print(res)
# print(front)
# print(back)