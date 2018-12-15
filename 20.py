a=raw_input()
b=len(a)
c=list(a)
for i in range(b):
    c[i]=ord(a[i])+3
for j in range(b):
    c[j]=chr(c[j])
print ''.join(c)
