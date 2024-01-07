from itertools import product

N = int(input())
R = list(input())
C = list(input())

L_A = []
L_B = []
L_C = []

def judge(L):
    f = True
    for i in range(N):
        tmp = set()
        for j in range(N):
            if L[j][i] == '.':
                continue
            if not tmp:
                if C[i] == L[j][i]:
                    tmp.add(L[j][i])
                else:
                    f = False
            else:
                if L[j][i] in tmp:
                    f = False
                else:
                    tmp.add(L[j][i])
        if not f:
            return f
    return f

for i in range(N-2):
    for j in range(i+1,N):
        for k in range(i+1,N):
            if j == k:
                continue
            tmp = ['.'] * N
            tmp[i] = 'A'
            tmp[j] = 'B'
            tmp[k] = 'C'
            L_A.append(tmp)
            tmp = ['.'] * N
            tmp[i] = 'B'
            tmp[j] = 'C'
            tmp[k] = 'A'
            L_B.append(tmp)
            tmp = ['.'] * N
            tmp[i] = 'C'
            tmp[j] = 'A'
            tmp[k] = 'B'
            L_C.append(tmp)


L = list(product(range(len(L_A)), repeat=N))
for l in L:
    tmp = []
    for i in range(N):
        if R[i] == 'A':
            tmp.append(L_A[l[i]])
        if R[i] == 'B':
            tmp.append(L_B[l[i]])
        if R[i] == 'C':
            tmp.append(L_C[l[i]])
    if judge(tmp):
        print('Yes')
        for l in tmp:
            print(*l, sep='')
        exit()
print('No')