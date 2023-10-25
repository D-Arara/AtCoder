def main():
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    graph = [[] for i in range(N)]

    for i in range(M):
        X, Y = map(int, input().split())
        graph[Y-1].append(X-1)
    
    res = - (1 << 62)
    for i in range(N):
        tmp = A[i]
        for j in graph[i]:
            res = max(A[i] - A[j], res)
            tmp = min(tmp, A[j])
        A[i] = tmp
    
    print(res)
    
if __name__ == "__main__":
    main()
