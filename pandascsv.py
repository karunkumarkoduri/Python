import pandas as pd

file=pd.read_csv("C:\\Users\\admin\\Desktop\\Python\\Week2.csv")

print("head of frame:")
print(file.head())

print("Tail of frame: ")
print(file.tail())

print("Information about frame: ")
print("file.info()")

print("Description of frame: ")
print(file.describe())