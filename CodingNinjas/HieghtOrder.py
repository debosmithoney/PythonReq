for _ in range(int(input())):
    h = list(map(int, input().strip().split()))
    o = list(map(int, input().strip().split()))
    for i in range(len(h)):
        
        if h[i]>=h[i+1]