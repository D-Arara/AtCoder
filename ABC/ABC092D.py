A, B = map(int, input().split())

ans = [['.']*100 for i in range(50)] + [['#']*100 for i in range(50)]

cnt_A = 0

for i in range(51,100,2):
    for j in range(0,100,2):
        if cnt_A == A - 1:
            break
        ans[i][j] = '.'
        cnt_A += 1
    else:
        continue
    break

cnt_B = 0

for i in range(0,50,2):
    for j in range(0,100,2):
        if cnt_B == B - 1:
            break
        ans[i][j] = '#'
        cnt_B += 1
    else:
        continue
    break

print(100, 100)
    
for i in ans:
    print(*i, sep='')

#ネタバレしたこれは思いつかないか