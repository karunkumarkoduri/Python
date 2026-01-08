#write a python program to find if a number is prime or not without recursion:
print("----WITHOUT RECURSION----")
def prime(num):
    if(num==0 or num==1):
        print(num,"is neither prime nor composite")
    else:
        count=0
        for i in range(1,num+1):
            if(num%i==0):
                count = count + 1
        if(count>2):
            print(num,"is not prime")
        else:
            print(num,"is prime")
num=int(input("Enter a non-negative integer:"))
if(num<0):
    print("Invalid input,I Asked To Enter a Non-Negative Number!")
else:
    prime(num)
#with recursion:
print("----WITH RECURSSION----")
def prime1(num,i=1,count=0):
    if(i>num):
        return count
    if(num%i==0):
        count += 1
    return prime1(num,i+1,count)
n=int(input("Enter a non-negative integer:"))
if(n<0):
    print("Invalid input,I Asked To Enter a Non-Negative Number!")
elif(n==0 or n==1):
     print(n,"is neither prime nor composite")
else:
    if(prime1(n)==2):
        print(n,"is prime")
    else:
        print(n,"is not a prime")