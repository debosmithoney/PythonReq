try:
    t= int(input())
    for i in range(0,t):
        g1,s1,b1,g2,s2,b2=map(int,input().strip().split())
        print(1 if (g1+s1+b1)>(g2+s2+b2) else 2)
except:
    pass