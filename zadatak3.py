x1=int(input("unesi x1:"))
y1=int(input("unesi y1:"))
x2=int(input("unesi x2:"))
y2=int(input("unesi y2:"))
k=(y2-y1)/(x2-x1)
l=k*x1+y1
if l<0:
    print("y=",k,"x",l)
elif l==0:
    print("y=",k,"x")
else:
    print("y=",k,"x+",l)