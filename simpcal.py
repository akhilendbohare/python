a=int(input("enter the number"))
b=int(input("enter the num2"))
ch=int(input("enter the number"))
print("\n2.addition\n3.substraction\n1.multiplication\n4.division")
if(ch==1):
    c=a*b
    print("mutiplication"+str(c))
elif(ch==2):
    c=a+b
    print("sum"+str(c))
elif(ch==3):
    c=a-b
    print("substraction"+str(c))
elif(ch==4):
    c=a/b
    print("division"+str(c))
else:
    print("choice")
