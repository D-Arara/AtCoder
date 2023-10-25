def main():
    import sys
    input = sys.stdin.readline
    
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    res = 0
    
    for i in range(1,h1-1):
        for j in range(1,h1-1):
            for k in range(1,h2-1):
                for l in range(1,h2-1):
                    a1 = h1 - i - j
                    if a1 <= 0:
                        continue
                    a2 = h2 - k - l
                    if a2 <= 0:
                        continue
                    a3 = w1 - i - k
                    if a3 <= 0:
                        continue
                    a4 = w2 - j - l
                    if a4 <= 0:
                        continue
                    a5 = h3 - a3 - a4
                    a6 = w3 - a1 - a2
                    if a5 >= 1 and a5 == a6:
                        res += 1
        
    print(res)
    
if __name__ == "__main__":
    main()
