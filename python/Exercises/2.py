#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num1 = int(input("Input a number from 1-10 here! : "))

if (num1 % 2) == 0:
    print(str(num1) + " is an even number!")
else: 
    print(str(num1) + " is not an even number!")

