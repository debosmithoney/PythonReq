try:
    for _ in range(int(input().strip())):
        n,p,k=map(int,input().strip().split())
        s=0
        a=p%k - 1
        b=(n-1)-((n-1)//k)*k
        s+=((b+1)*((n-1)//k + 1) + (a-b)*((n-1)//k)) if a>b else (((n-1)//k + 1)*(a+1))

        for i in range(a+1,n,k):
            s+=1
            if(i==p):
                print(s)
                break
except:
    pass