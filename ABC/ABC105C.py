N = int(input())

ans = ''

if N == 0:
    print(0)
else:
    while N != 0:
        r = N % 2
        if r < 0:
            r += 2
        N = (N - r) // (-2)
        ans += str(r)

    print(ans[::-1])    
