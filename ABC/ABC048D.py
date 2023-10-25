s = input()

flag = 1

if len(s) % 2:
    flag *= -1
if s[0] != s[-1]:
    flag *= -1

if flag == 1:
    print('First')
else:
    print('Second')