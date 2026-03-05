#Write a program to implement seek(), tell() and flush() methods with different arguments in a file.
import time
f1=open("example","w+")
f1.write("Mr KKK")
print(f1.tell()) #returns the current position of the file pointer
f1.seek(3) #moves to the 3rd byte
print(f1.read())
f1.write("\nHello world")
f1.flush()
time.sleep(2)
f1.write("\nkarun")
print(f1.read())