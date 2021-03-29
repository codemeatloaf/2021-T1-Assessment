# Create a program that asks the user for a number and then prints out a list of all the divisors of that number

num1 = int(input("Input a number here! : "))

listRange = list(range(1,num1+1))

divisorList = []

for number in listRange:
    if num1 % number == 0:
        divisorList.append(number)

print(divisorList)