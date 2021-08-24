try:
    t=int(input().strip())
    c=su=0
    su1=999999
    for i in range(0,t):
        n=int(input().strip())
        a =list(map(int,input().strip().split()))
        for k in range(0,len(a)):
            su=min((a[k] | a[c]),su1);
        c+=1
        su1=su
    print(su1)
except:
    pass