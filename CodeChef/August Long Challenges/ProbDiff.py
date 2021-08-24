try:
    t=int(input())
    for i in range(0,t):
        a=list(map(int,input().strip().split()))
        s=set(a)
        if (len(s)==4 or len(s)==3):
            print(2)
        elif (len(s)==2):
            print(2 if(a.count(a[0]) == 2) else 1)
        else:
            print(0)
except:
    pass