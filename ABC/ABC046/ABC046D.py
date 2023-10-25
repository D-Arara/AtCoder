s = input()
G = s.count('g')
P = len(s) - G
if len(s) % 2 == 0:
    print(len(s)//2 - P)
else:
    print((len(s)-1)//2 - P)