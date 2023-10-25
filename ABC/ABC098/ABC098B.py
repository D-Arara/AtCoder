def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(1,N):
        tmp = set(S[:i]) & set(S[i:])
        ans = max(ans,len(tmp))
    print(ans)

if __name__ == '__main__':
    main()
