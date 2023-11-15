A, B, C, D = map(int, input().split())
# O(√N)
def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(A,B+1):
    f = True
    for j in range(C,D+1):
        if is_prime(i+j):
            f = False
            break
    if f:
        print('Takahashi')
        exit()
print('Aoki')