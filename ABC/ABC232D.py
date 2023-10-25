def main():
    from collections import deque

    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]

    q = deque()
    q.append((0,0))

    dist = [[0]*W for i in range(H)]
    dist[0][0] = 1
    ans = 1

    while q:
        h, w = q.popleft()
        d = dist[h][w]
        if h + 1 < H and C[h+1][w] == '.':
            if dist[h+1][w] < d + 1:
                dist[h+1][w] = d + 1
                q.append((h+1,w))
        if w + 1 < W and C[h][w+1] == '.':
            if dist[h][w+1] < d + 1:
                dist[h][w+1] = d + 1
                q.append((h,w+1))

    ans = 0

    for i in range(H):
        for j in range(W):
            ans = max(ans, dist[i][j])

    print(ans)

if __name__ == '__main__':
    main()