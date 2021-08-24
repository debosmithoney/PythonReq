try:
    t=int(input())
    wl=0
    for i in range(0,t):
        n,d,h=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        for j in range(0,n):
            if a[j]>0:
                wl+=a[j]
            elif a[j] == 0:
                wl-= wl if wl<d else d
            
        print("YES" if wl>h else "NO")
        wl=0
except:
    pass
