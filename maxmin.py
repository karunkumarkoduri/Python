a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
c=int(input("Enter number3:"))
if(a>b & a>c):
    print(a,"is maximun")
    if(b>c):
        print(c,"is minimum")
    else:
        print(b,"is minimum")
elif(b>c):
    print(b,"is maximum")
    if(a<b & a<c):
        print(a,"is minimum")
    else:
        print(c,"is minimum")
else:
    print(c,"is maximum")
    if(a<b):
        print(a,"is minimum")
    else:
        print(b,"is minimum")