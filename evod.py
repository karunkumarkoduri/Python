a=int(input("Enter range:"))
count1=0
count2=0
for i in range(1,a+1):
    if(i%2 == 0):
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print("number of Evens:",count1)
print("number of odds:",count2)