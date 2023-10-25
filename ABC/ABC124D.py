from itertools import accumulate

N, K = map(int, input().split())
S = input()


T = [0]
R = [0]
cnt = 1

for i in range(1,N):
    if S[i-1] != S[i]:
        if S[i-1] == '0':
            T.append(cnt)
        else:
            R.append(cnt)
        cnt = 1
    else:
        cnt += 1
    
if S[-1] == '0':
    T.append(cnt)
else:
    R.append(cnt)

if S[0] == '0':
    R = [0] + R
if S[-1] == '0':
    R = R + [0]

if K == 0:
    print(max(R))
    
tmp_T = sum(T[:K])
tmp_R = sum(R[:K+1])
ans = tmp_T + tmp_R

for i in range(len(T)-K):
    tmp_T += T[i+K] - T[i]
    tmp_R += R[i+K+1] - R[i]
    ans = max(ans, tmp_T+tmp_R)
    
print(ans)