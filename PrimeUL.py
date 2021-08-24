d=e=0
for i in range(int(input("Enter Lower range: ")),int(input("Enter Higher range: "))):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        d=d+1
        print(i,end=" ")
        e+=1 if i>9 and i<100 else 0
print("\nNumber of Prime Numbers: ",d)
print("Number of 2 Digit Prime Numbers: ",e)