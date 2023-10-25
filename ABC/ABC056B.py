W, a, b = map(int, input().split())
print(max(b-a-W, a-b-W, 0))