def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    
    N, K = map(int, input().split())
    A = set(map(int, input().split()))
    post = [tuple(map(int, input().split())) for i in range(N)]
    D = defaultdict(lambda: 1<<61)
    res = 0
    
    def dist(a, b):
        x = (a[0] - b[0]) ** 2
        y = (a[1] - b[1]) ** 2
        return (x + y) ** 0.5
    
    for i in range(N):
        if not i + 1 in A:
            continue
        for j in range(N):
            if j + 1 in A:
                continue
            D[post[j]] = min(D[post[j]], dist(post[i], post[j]))
    
    print(max(D.values()))
    
if __name__ == "__main__":
    main()
