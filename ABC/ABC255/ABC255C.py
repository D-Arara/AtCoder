def main():
    import sys
    input = sys.stdin.readline
    
    X, A, D, N = map(int, input().split())
    B = A + (N - 1) * D
    if D >= 0:
        if X <= A:
            print(A-X)
        elif B <= X:
            print(X-B)
        else:
            X -= A
            num = X // D
            print(min(X-num*D, (num+1)*D-X))
    else:
        if X <= B:
            print(B-X)
        elif A <= X:
            print(X-A)
        else:
            X -= A
            num = X // D
            print(min(num*D-X, X-(num+1)*D))

if __name__ == "__main__":
    main()
