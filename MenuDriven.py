n= int(input())
x=input()
if x == 'a':
    f=lambda n: 1 if n < 2 else n*f(n-1)
    print(f(n))
elif x == 'b':
    print(str(n)[::-1])
elif x == 'c':
    print("Factors of ",n," : ")
    for i in range(1,n+1):
        if n%i == 0: print(i,end=" ")