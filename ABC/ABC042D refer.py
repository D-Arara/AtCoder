def power_func(a,b,p):
  """a^b mod p を求める"""
  if b==0: return 1
  if b%2==0:
    d=power_func(a,b//2,p)
    return d*d %p
  if b%2==1:
    return (a*power_func(a,b-1,p ))%p

H,W,A,B=map(int, input().split())
p=10**9+7
ans=0
X=[1]  #階乗テーブル
for i in range(1,H+W-1):
  X+=[ (X[-1]*i) %p ]
Y=[1]*(H+W-1)  #階乗の逆元テーブル
Y[H+W-2]=power_func(X[H+W-2],p-2,p)
for i in range(H+W-3,-1,-1):
  Y[i]=Y[i+1]*(i+1) %p
for i in range(B,W):
  ans+=(X[H-A-1+i]*X[A+W-2-i]*Y[H-A-1]*Y[i]*Y[A-1]*Y[W-1-i])%p

print(ans%p)