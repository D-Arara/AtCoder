s = input()
for i in range(0,len(s)-2,2):
    if s[i] == s[i+2]:
        i += 1
        print(i, i+2)
        exit()
for i in range(1,len(s)-2,2):
    if s[i] == s[i+2]:
        i += 1
        print(i, i+2)
        exit()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        i += 1
        print(i, i+1)
        exit()
print(-1, -1)