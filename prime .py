n=int(input("enter the number="))
if n>1:
    for i in range(2,(n//2)+1):
        if(n%i)==0:
            print(n,"not prime number")
            break
        else:
            print(n,"is a prime number")
else:
    print(n,"is mot prime num")
