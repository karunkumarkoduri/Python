print("---Difference between LIst comprehension and Dictionary comprehension---")
nums=[1,2,3,4,5]
print("Numbers:",nums)
lst_comp=[n*2 for n in nums]
dict_comp={n:n*2 for n in nums}
print("List comprehension:",lst_comp)
print("Dictionary comprehension:",dict_comp)