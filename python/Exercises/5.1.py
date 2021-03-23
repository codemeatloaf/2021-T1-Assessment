# Write a program that returns a list that contains only the elements that are common between the lists. Randomly generate the two lists
import random

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
d = random.randint(0,100)
e = random.randint(0,100)
f = random.randint(0,100)
g = random.randint(0,100)
h = random.randint(0,100)
i = random.randint(0,100)
j = random.randint(0,100)
k = random.randint(0,100)
l = random.randint(0,100)
m = random.randint(0,100)
n = random.randint(0,100)
o = random.randint(0,100)
p = random.randint(0,100)

list1 = [h, i, j, k, l, m, n, o, p]
list2 = [a, b, c, d, e, f, g,]

common = set(list1).intersection(list2)

print(str(list1) + " Is list 1")
print(str(list2) + " Is list 2")
print(common)