#Write a program to implement read(), readline(), readlines(), write(), writelines() methods on files.

file1= open("demo","w")
file1.write("---hello world\n")
file1.write("this is python\n")
file1.write("A programming language\n")
lines=["line1\n","line2\n","line3---;"]
file1.writelines(lines)
file1.seek(0)
file1= open("demo","r")
print(file1.read())
file1.seek(0)
print(file1.readline())
file1.seek(0)
print(file1.readlines())