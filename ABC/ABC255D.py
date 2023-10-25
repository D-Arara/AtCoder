from posixpath import split


def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left
    from itertools import accumulate
    
    N, Q = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = [0] + list(accumulate(A))
    C = list(accumulate(A[::-1]))[::-1] + [0]

    for i in range(Q):
        X = int(input())
        num = bisect_left(A, X)
        tmp_1 = X * num - B[num]
        tmp_2 = C[num] - X * (N - num)
        print(tmp_1+tmp_2)
    
if __name__ == "__main__":
    main()
