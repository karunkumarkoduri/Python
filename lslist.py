lst=[]
n=int(input("Enter no. of elements in list:"))
print("Enter",n,"elements:")
for i in range(n):
    lst.append(int(input()))
print("Largest Element:",max(lst))
print("Smallest Element:",min(lst))