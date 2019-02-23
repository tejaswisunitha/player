#ma
n,k=map(int,input().split())
N=[int(x) for x in input().split()]
k=[int(x) for x in input().split()]
l1=[]
for i in range(0,len(k)):
	N.append(k[i])
	a=max(N)
	l1.append(a)
for i in range(0,len(l1)-1):
	print(l1[i],end=" ")
print(l1[-1])


