s='07:05:45PM'
t=s.split(':')
if s[-2] == 'P':
    if t[0] != "12":
        t[0] = str(int(t[0])+12)
else:
    if t[0] == '12':
        t[0] = '00'
print (str(':'.join(t)[:-2]))
