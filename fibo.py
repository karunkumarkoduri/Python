#fibonacii:
#with recurssion:
print("----With recursion----")
n=int(input("Enter a non-negative number:"))
if(n<0):
    print("Invalid input! Negative number entered")
else:
    print("Fibonacci series:",end=" ")
    def fibo(num):
        if(num==0):
            return 0
        elif(num==1):
            return 1
        else:
            return fibo(num-1)+fibo(num-2)
    for i in range(n):
        print(fibo(i),end=" ")
#using iteration:
print("\n----With iteration----")
nm=int(input("Enter a non-negative number:"))
if(nm<0):
    print("Invalid input! Negative number entered.")
else:
    a,b=0,1
    print("Fibonacci series:",end=" ")
    for i in range(nm):
        print(a,end=" ")
        c=a+b
        a=b
        b=c