x,s=int(input("Enter a Number: ")),0
m=x
while m>0:
    r = m%10
    s+=r ** len(str(x))
    m//=10

if s==x:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
