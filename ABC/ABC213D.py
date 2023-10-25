def main():
    from collections import deque

    N = int(input())

    G = [[] for i in range(N+1)]

    for i in range(N-1):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)

    q = deque([1])
    seen = [False]*(N+1)
    seen[1] = True
    ans = []

    while q:
        v = q.pop()
        if v < 0:
            ans.append(-v)
        else:
            ans.append(v)
            c = sorted(G[v], reverse=True)
            for to in c:
                if seen[to]:
                    continue
                seen[to] = True
                q.append(-v)
                q.append(to)

    print(*ans)

if __name__ == '__main__':
    main()