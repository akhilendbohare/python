a=int(input ("enter the number"))
b=int(input ("enter the number"))
c=int(input ("enter the number"))
if((a>b)and(a>c)):
    print (a,"a is greater")
elif((b>a)and(b>c)):
    print(b,"b is greater")
elif((c>a)and(c>b)):
    print(c,"c is greater")
else:
    print("all are equal")
