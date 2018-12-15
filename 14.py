x=raw_input()
n=len(x)
e=''
for  y in range(-1,-(n+1),-1):
    if x[y]!='a' and x[y]!='e' and x[y]!='i' and x[y]!='o' and x[y]!='u':
        z=x[y]
        e=e+z
print(e)
