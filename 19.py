a=int(raw_input())
x=1
while(x<=a):
    z=0
    if(a%x==0):
        y=1
        while(y<=x):
            if(x%y==0):
                z=z+1
            y=y+1
        if(z==2):
            print(x),
    x=x+1
