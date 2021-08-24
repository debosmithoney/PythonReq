from math import *
try:
    t=int(input())
    for j in range(t):
        n, k = map(int, input().split())
        s = list(map(int, input().split()))
        bits = [0]*(32)
        for i in range(32):
            for q in s:
                if q & (1 << i):
                    bits[i] += 1
        sm = 0
        for q in bits:
            sm += ceil(q/k)
        print(sm)
except:
    pass