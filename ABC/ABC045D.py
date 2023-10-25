def main():    
    from collections import defaultdict, Counter

    H, W, N = map(int, input().split())

    D = defaultdict(int)

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(-1,2):
            for k in range(-1,2):
                if 2 <= a + j <= H - 1 and 2 <= b + k <= W - 1:
                    D[(a+j,b+k)] += 1

    C = Counter(D.values())

    print((H-2)*(W-2) - sum(C.values()))

    for i in range(1,10):
        print(C[i])

if __name__ == '__main__':
    main()