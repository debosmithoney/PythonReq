try:
    t=int(input())
    for i in range(0,t):
        a=list(map(int,input().strip().split()))
        a.sort()
        print(sum(a[1:3]))
except:
    pass