v,k=raw_input().split()
v=int(v)
k=int(k)
l=[]
if v==1 or k==1:
	print "1"
else:
	for i in range(2,v*k):
		if (v%i==0 and k%i==0):
			l.append(i)
	print max(l)
