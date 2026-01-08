#with recursion:
print("----With Recursion----")
def factwr(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*factwr(num-1)
n=int(input("Enter a non-negative Integer:"))
if(n<0):
    print("Invalid input!")
else:
    print("Factorial of",n,"is",factwr(n))
#without Recursion
print("----Without Recursion----")
def factwor(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)
nm=int(input("Enter a non-negative Integer:"))
if(nm<0):
    print("Invalid input!")
else:
    factwor(nm)
    