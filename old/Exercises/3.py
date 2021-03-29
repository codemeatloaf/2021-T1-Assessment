# write a program that prints out all the elements of a list that are less than 5

lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = lst1.copy()

lst2.remove(1)
lst2.remove(1)
lst2.remove(2)
lst2.remove(3)
lst2.remove(5)

print("List: ", lst1)
print("Lists with everything below 5 removed: ",lst2)
 