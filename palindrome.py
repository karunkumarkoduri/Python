n=input("Enter a string:")
n= n.lower()
l=len(n)
c=0
for i in range(l):
    if(n[i]==n[l-i-1]):
        c+=1
if(c==l):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")