p,d,m,s=map(int,input().strip().split())
while(s):
    print(p+((p-d) if p>m else m))
    s-=p
    