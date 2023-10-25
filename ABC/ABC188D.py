def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    
    N, C = map(int, input().split())
    D = defaultdict(int)
    
    for i in range(N):
        a, b, c = map(int, input().split())
        D[a] += c
        D[b+1] -= c

    key = sorted(D.keys()) + [0]
    price = 0
    res = 0
    for i in range(len(key)-1):
        res += min(price, C) * (key[i] - key[i-1])
        price += D[key[i]]
        
    print(res)
    
if __name__ == "__main__":
    main()
