def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    A = list(map(int, input().split()))
    tmp = []
    M = min(3, N)
    for i in A[-M:]:
        tmp.append(0)
        for j in range(len(tmp)):
            tmp[j] += i
    for i in tmp:
        if i < 4:
            N -= 1
    print(N)
        
    
if __name__ == "__main__":
    main()
