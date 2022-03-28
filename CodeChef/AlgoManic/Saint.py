for _ in range(int(input())):
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    print('Pass' if sum(a)==sum(b) else 'Fail')