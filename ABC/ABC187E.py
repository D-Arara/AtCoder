def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    edge = []
    graph = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge.append((a, b))
        graph[a].append(b)
        graph[b].append(a)
        
    q = [0]
    depth = [-1] * N
    depth[0] = 0
    
    while q:
        v = q.pop()
        for to in graph[v]:
            if depth[to] != -1:
                continue
            depth[to] = depth[v] + 1
            q.append(to)
    
    c = [0] * N
    Q = int(input())
    for i in range(Q):
        t, e, x  = map(int, input().split())
        a, b = edge[e-1]
        if depth[a] > depth[b]:
            a, b = b, a
            t ^= 3
        if t == 1:
            c[0] += x
            c[b] -= x
        else:
            c[b] += x
    
    q = [0]
    while q:
        v = q.pop()
        for to in graph[v]:
            if depth[v] < depth[to]:
                c[to] += c[v]
                q.append(to)
    for i in c:
        print(i)
    
if __name__ == "__main__":
    main()
