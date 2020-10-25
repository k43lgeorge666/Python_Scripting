#!/usr/bin/python

list1 = []

quantity = input("How may numbers do you want to enter?: ")
for i in range (quantity):
	number = input("Enter the element number " + str(i) + " in the list: ")
	list1.append(number)

print("")
print("------ The elements in the list -------- ")
print(str(list1))
print("")