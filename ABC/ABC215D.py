def main():
    def make_divisors(n,S):
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                S.add(i)
                if i != n // i:
                    S.add(n//i)

    def sieve(n, L):
        is_prime = [True for _ in range(n+1)]
        for i in L:
            if i == 1:
                continue
            cnt = i
            while i <= n:
                is_prime[i-1] = False
                i += cnt
        table = [ i for i in range(1, n+1) if is_prime[i-1]]
        return table
    
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    S = set()
    ans = []

    for i in A:
        make_divisors(i,S)

    S = sorted(list(S))
    ans = sieve(M, S)

    print(len(ans))

    for i in ans:
        print(i)

if __name__ == "__main__":
    main()