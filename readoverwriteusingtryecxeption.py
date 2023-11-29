read

f1=open("file.txt","r")
data=f1.read()
print(data)
overwrite using error function
f=input("Enter the filename:")
try:
    fileptr=open(f,"r")
    data=fileptr.read()
    print(data)
    try:
        fileptr=open("file.txt","w")
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error") 
