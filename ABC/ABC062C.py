H, W = map(int, input().split())
if H % 3 == 0 or W % 3 == 0:
    print(0)
else: 
    ans = []

    x = 2 * W // 3
    for i in range(x,x+2):
        L = []
        tmp = H // 2
        L.append((W - i) * H)
        L.append(i * (H - tmp))
        L.append(i * tmp)
        ans.append(max(L) - min(L))

    y = 2 * H // 3
    for i in range(y,y+2):
        L = []
        tmp = W // 2
        L.append((H - i) * W)
        L.append(i * (W - tmp))
        L.append(i * tmp)
        ans.append(max(L) - min(L))                                       
        
    ans.append(min(H,W))

    print(min(ans))