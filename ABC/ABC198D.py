import itertools

S = []
keys = set()
alph = [-1]*26

for i in range(3):
    s = input()
    keys |= set(s)
    S.append(s)

keys = list(keys)

if len(keys) > 10:
    print('UNSOLVABLE')
    exit()

p = itertools.permutations(list(range(10)), len(keys))

for i in p:
    for k in range(len(keys)):
        alph[ord(keys[k])-ord('a')] = i[k]
    ans = [0]*3
    for i in range(3):
        for j in range(len(S[i])):
            if j == 0 and alph[ord(S[i][j])-ord('a')] == 0:
                break
            ans[i] += alph[ord(S[i][j])-ord('a')] * (10 ** (len(S[i])-j-1))
        else:
            continue
        break
    else:
        if ans[0] + ans[1] == ans[2]:
            for i in ans:
                print(i)
            exit()

print('UNSOLVABLE')