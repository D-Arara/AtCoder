from collections import deque

X = int(input())

q = deque(range(1,100))

while q:
    num = q.popleft()
    if num >= X:
        print(num)
        exit()
    if num >= 10:
        m = num % 10
        n = (num // 10) % 10
        new = 2 * m - n
        if 0 <= new <= 9:
            q.append(num * 10 + new)