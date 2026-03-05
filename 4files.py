import os
import shutil
f=open("copymoveremove.txt","w")
f.write("Hello KKK")
f.close()
shutil.copy("copymoveremove.txt","copy.txt")
print("File copied.")
shutil.move("copymoveremove.txt","moved.txt")
print("File moved.")
os.remove("moved.txt")
print("File removed.")