#!/usr/bin/python
list1 = []
total = 0
quantity = input("How many employees's salaries you want to enter?: ")
for i in range (quantity):
	print("")
	salary = float(input("Enter the salary for the employee number " + str(i) + ": ")) 
	list1.append(salary)
	total = total + salary / quantity
print("")
print("------ Salaries and salaries average --------")
print("")
print(str(list1))
print(str(total))

