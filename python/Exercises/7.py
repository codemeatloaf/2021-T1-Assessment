# Write one line of Python that takes a list and makes a new list that has only the even 
# elements of this list in it

# list1 = input("Input the elements of the list seperated by spaces: ")
# list2 = list1.split()
list3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(list(num for num in list3 if num % 2 == 0))
