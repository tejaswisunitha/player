r=raw_input()
b=len(r)
c=list(r)
for i in range(b):
    c[i]=ord(r[i])+3
for j in range(b):
    c[j]=chr(c[j])
print ''.join(c)
