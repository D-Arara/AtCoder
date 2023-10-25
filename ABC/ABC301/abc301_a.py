N = int(input())
S = list(input())
a = S.count('T')
if N % 2 == 0 and a == N // 2:
    if S[-1] == 'A':
        print('T')
    else:
        print('A')
elif a > N / 2:
    print('T')
else:
    print('A')
    