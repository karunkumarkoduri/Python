#Write a program to generate 20 random numbers in the range of 1 to 100 and write to a file.
import random as r 
f=open("randinfile","w+")
for i in range(20):
    a=r.randint(1,100)
    f.write(a)
    f.write("\n")