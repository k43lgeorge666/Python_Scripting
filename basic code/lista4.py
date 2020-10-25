#!/usr/bin/python

x=0
list1 = []

quantity = input("How many numbers do you want to add to the list?: ")
while x<quantity:
	number = input("Enter the element number " + str(x) + " in the list: ")
	list1.append(number)
	x = x + 1
print("------ The elements in the list --------")
print(str(list1))
print("")

