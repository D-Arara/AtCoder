N, K = map(int,input().split())
D = set(input().split())
while 1:
    tmp = set(str(N))
    if len(tmp|D) == len(tmp) + len(D):
        print(N)
        exit()
    N += 1