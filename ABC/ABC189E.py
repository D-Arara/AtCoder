def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    xy = [tuple(map(int, input().split())) for i in range(N)]
    
    M = int(input())
    O = [list(input().split()) for i in range(M)]
    
    Q = int(input())
    ab = []
    for i in range(Q):
        a, b = map(int, input().split())
        ab.append((a, b, i))
    ab.sort()
    
    def matrix_prod(m1, m2):
        m3 = [[0]*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                tmp = 0
                for k in range(3):
                    tmp += m1[i][k] * m2[k][j]
                m3[i][j] = tmp
        return m3

    res = [(0, 0) for i in range(Q)]
    m1 = [[1,0,0], [0,1,0], [0,0,1]]
    cnt = 0
    for i in range(Q):
        a, b, n = ab[i]
        while cnt < a:
            op = O[cnt]
            if op[0] == '1':
                m2 = [[0,1,0], [-1,0,0], [0,0,1]]
            elif op[0] == '2':
                m2 = [[0,-1,0], [1,0,0], [0,0,1]]
            elif op[0] == '3':
                p = int(op[1])
                m2 = [[-1,0,2*p], [0,1,0], [0,0,1]]
            else:
                p = int(op[1])
                m2 = [[1,0,0], [0,-1,2*p], [0,0,1]]
            m1 = matrix_prod(m2, m1)
            cnt += 1
        x, y = xy[b-1]
        x1 = m1[0][0] * x + m1[0][1] * y + m1[0][2]
        y1 = m1[1][0] * x + m1[1][1] * y + m1[1][2]
        res[n] = (x1, y1)
        
    for x, y in res:
        print(x, y)
    
if __name__ == "__main__":
    main()
