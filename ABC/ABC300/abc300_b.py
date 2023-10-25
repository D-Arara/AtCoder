H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) * 2 for _ in range(H)]

for i in range(H):
    tmp = A.pop(0)
    A.append(tmp)
    num = -1
    for j in range(W):
        if A[0] == B[0][j:j+W]:
            for k in range(H):
                if A[k] != B[k][j:j+W]:
                    break
            else:
                print('Yes')
                exit()
print('No')
    