from collections import defaultdict

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

q = []
D = defaultdict(int)

