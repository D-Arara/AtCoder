S = set(input())
if len(S) == 26:
    print('None')
else:
    L = [chr(i) for i in range(97, 122)]
    L = set(L)
    L -= S
    print(sorted(list(L))[0])