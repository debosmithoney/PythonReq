for _ in range(int(input().strip())):
    n=int(input().strip())
    s=0
    for c in range(1,n+1):
        for b in range(c,n+1,c):
            if b%c == 0:
                for a in range(c,n+1,b):
                    s+=1 if a%b == c else 0
    print(s)