import pandas as pd
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age":  [25, 32, 18, 47, 33],
    "Score": [88, 92, 85, 90, 85]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nSorted by Score (ascending):")
sorted1 = df.sort_values(by="Score")
print(sorted1)
print("\nSorted by Age (descending):")
sorted2 = df.sort_values(by="Age", ascending=False)
print(sorted2)
print("\nSlicing first 3 rows (using slicing):")
slice1 = df[:3]
print(slice1)
print("\nSlicing rows 1 to 3 (using .iloc):")
slice2 = df.iloc[1:4]
print(slice2)
print("\nSlicing rows and columns (rows 0–2, columns 'Name' and 'Age') using .loc:")
slice3 = df.loc[0:2, ["Name", "Age"]]
print(slice3)