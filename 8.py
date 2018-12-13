try:
	s1=raw_input()
	a=s1.split(' ')
	g=" "
	for i in range(0,len(a)):
			a[i]=a[i].capitalize()
	d=a[0]
	for i in range(1,len(a)):
		d=d+g+a[i]
	print d
except:
	print "Invalid"
