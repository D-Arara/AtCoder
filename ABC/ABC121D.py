A, B = map(int, input().split())
A -= 1

if A % 2 == 0:
    if A % 4 != 0:
        A = A ^ 1
else:
    if (A+1) % 4 == 0:
        A = 0
    else:
        A = 1

if B % 2 == 0:
    if B % 4 != 0:
        B = B ^ 1
else:
    if (B+1) % 4 == 0:
        B = 0
    else:
        B = 1

print(A^B)