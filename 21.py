x1,y1=map(int,raw_input().split(' '))
x2,y2=map(int,raw_input().split(' '))
x3,y3=map(int,raw_input().split(' '))
if (x1==x2 and x2==x3) or(y1==y2 and y2==y3) or (abs(x1-x2)==abs(x2-x3) and abs(y1-y2)==abs(y2-y3)):print("yes")
else:print("no")
