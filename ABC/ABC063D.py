N, A, B = map(int, input().split())
h = [int(input()) for i in range(N)]

def f(x):
    cnt = x
    for i in range(N):
        if h[i] <= B * x:
            continue
        cnt -= -(-(h[i] - B * x) // (A - B))
        if cnt < 0:
            return False
    return True

left = 0
right = max(h) // B + 1

while right > left:
    mid = (left + right) // 2
    if f(mid):
        right = mid
    else:
        left = mid + 1

print(left)
