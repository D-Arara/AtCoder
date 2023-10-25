N = int(input())
T = input()

flag = 0
x, y = 0, 0

for i in T:
    if i == 'R':
        i += 1
        i %= 4
    if i == 'S':
        if i == 0:
            x += 1
        elif i == 1:
            y += 1
        elif i == 2:
            x -= 1
        elif i == 3:
            y -= 1
            
print(x, y)