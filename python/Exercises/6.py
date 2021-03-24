# Ask the user for a string and print out whether this string is a palindrome or not

list1 = input("Input the elements of the list seperated by spaces: ")
list2 = list1.split()

def isPalindrome(s):
    return s == s[::-1]

# to test that it works splits it into a list
# print("List: ", list2) 

s = list2

ans = isPalindrome(s)

if ans:
    print(str(list2) + " Is a palindrome" )
else:
    print(str(list2) + " Is not a palindrome")
