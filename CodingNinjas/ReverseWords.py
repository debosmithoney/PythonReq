for _ in range(int(input())):
    n= list(map(str,input().strip().split()))
    n=n[::-1]
    print(' '.join(map(str,n)))