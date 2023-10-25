from bisect import bisect_left

A, B, Q = map(int, input().split())
s = [int(input()) for i in range(A)]
t = [int(input()) for i in range(B)]

def f(x):
    ans = 2 * 10 ** 10
    num_s = bisect_left(s, x)
    num_t = bisect_left(t, x)
    
    if num_s != A and num_t != B:
        ans = min(ans, max(s[num_s]-x, t[num_t]-x))
    if num_s != 0 and num_t != 0:
        ans = min(ans, max(x-s[num_s-1], x-t[num_t-1]))
    if num_s != 0 and num_t != B:
        ans = min(ans, 2*min(x-s[num_s-1],t[num_t]-x)+max(x-s[num_s-1],t[num_t]-x))
    if num_s != A and num_t != 0:
        ans = min(ans, 2*min(s[num_s]-x,x-t[num_t-1])+max(s[num_s]-x,x-t[num_t-1]))
    
    return ans

for i in range(Q):
    x = int(input())
    print(f(x))