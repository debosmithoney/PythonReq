t=int(input())
while(t>0):
    n,k=map(int,input().split())
    A=[]
    for i in range(k,n+1,k):
        A.append(i)
    while len(A)>=k:
        B=[]
        for j in range(k-1,len(A),k):
            B.append(A[j])
        A=B
    print(A[0])