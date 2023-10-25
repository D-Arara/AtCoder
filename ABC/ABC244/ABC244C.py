N = int(input())
L = [True] * (2 * N + 2)
cnt = 1
 
for i in range(N+1):
    while not L[cnt-1]:
        cnt += 1
    print(cnt, flush=True)
    L[cnt-1] = False
    A = int(input())
    L[A-1] = False