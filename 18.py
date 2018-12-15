num=[]
l=[]
count=0
n=int(raw_input())
for i in xrange(0, n):
    num.append(raw_input())
for i in range(0,n):
    l.append(list(num[i]))
for i in range(0,n):
    l.append(l[i].sort())
m=l[0]
for i in range(n+1):
    if m==l[i]:
        count=count+1
print count
