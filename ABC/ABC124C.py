S = input()
N = len(S)

cnt_0 = 0

for i in range(N):
    if i % 2 == 0:
        if S[i] != '0':
            cnt_0 += 1
    else:
        if S[i] != '1':
            cnt_0 += 1

cnt_1 = 0

for i in range(N):
    if i % 2 == 0:
        if S[i] != '1':
            cnt_1 += 1
    else:
        if S[i] != '0':
            cnt_1 += 1

print(min(cnt_0, cnt_1))