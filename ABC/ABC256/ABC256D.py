def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    
    S = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        L, R = map(int, input().split())
        S[L] += 1
        S[R] -= 1
        
    pre = 0
    for i in range(1,2*10**5+1):
        S[i] += S[i-1]
        if pre == 0 and S[i] != 0:
            pre = i
        if pre != 0 and S[i] == 0:
            print(pre,i)
            pre = 0
            
if __name__ == "__main__":
    main()
