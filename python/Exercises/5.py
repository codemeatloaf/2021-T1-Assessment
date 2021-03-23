# write a program that returns a list that contains only the elements that are common between the lists

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = set(list1).intersection(list2)

print(str(list1) + " Is list 1")
print(str(list2) + " Is list 2")
print(str(common) + " Is what they have in common")
