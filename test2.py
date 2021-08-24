d={0:0,1:1}
def fib(n):
  if n not in d:
    v=fib(n-1)+fib(n-2)
    d[n]=v
  return d[n]
n=int(input("ENTER THE VALUE OF n: "))
print("FIB(",n,")=",fib(n))