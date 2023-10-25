from heapq import heappush


def main():
    import heapq

    N = int(input())
    L = [list(map(int, input().split())) for i in range(N)]

    ans = 0
    flag = [False]*N
    flag[N-1] = True
    q = [-(N-1)]

    while q:
        v = -heapq.heappop(q)
        ans += L[v][0]
        for i in range(L[v][1]):
            if flag[L[v][i+2]-1]:
                continue
            flag[L[v][i+2]-1] = True
            heappush(q, -(L[v][i+2]-1))
    

    print(ans)


if __name__ == '__main__':
    main()