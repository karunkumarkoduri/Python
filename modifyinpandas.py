import pandas as pd

data={"NAME": ["A","B","C"],
      "AGE":[19,20,None],
      "CITY": ["vizag",None,"Amp"]
      }
file=pd.DataFrame(data)

file["NAME"].fillna("Unknown")
file["AGE"].fillna(0)
print("After cleaning DataFrame:")
print(file)

file["colleges"]="MVGR"
file.rename(columns={"AGE":"Years"},inplace=True)
print("Data after Modification: ")
print(file)