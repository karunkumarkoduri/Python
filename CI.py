#Write a python program to calculate compound interest
p=int(input("Enter principal(p):"))
r=int(input("rate of intrest(r):"))
n=int(input("Enter frequence(n):"))
t=int(input("Enter Time(t):"))
print("Compound Interest:",p*(1+r/n)**(n*t))
