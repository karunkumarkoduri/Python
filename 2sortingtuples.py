print("Sorting the tuple elements")
tuples_list = [(1, 2, 3), (4, 5, 1), (7, 8, 2), (9, 10, 4), (11, 12, 0)]
print("Original list:", tuples_list)
tuples_list.sort(key=lambda x: x[-1])
print("Sorted by last element:", tuples_list)
