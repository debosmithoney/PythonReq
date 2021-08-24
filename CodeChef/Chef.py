# cook your dish here
def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)
            

t=int(input())
for i in range(0,t):
        x,y=map(int,input().split())
            
if gcd(x,y)>1:
        print(0)
else:
    if gcd(x,y+1)>1:
        print(1)
    elif gcd(x+1,y)>1:
        print(1)