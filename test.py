print("ENTER -1 TO EXIT.")
c={}
while True:
  r=float(input ("ENTER THE RADIUS : "))
  if r == -1:
    break
  else:
    Dict={r:2*3.14*r}
    c.update(Dict)
print(c)