try:
    t=int(input())
    for i in range(0,t):
        s=0
        n=int(input())
        a=list(map(int,input().strip().split()))
        for i in range(0,n):
            for j in range(0,n):
                if i!=j:
                    s+= 1 if ((a[i]-a[j])/a[i] < (a[i]-a[j])/a[j]) else 0
        print(s)
except:
    pass