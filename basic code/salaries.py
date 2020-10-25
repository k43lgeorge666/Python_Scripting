#!/usr/bin/python

x=1
salary1 = 0
salary2 = 0
total = 0
numbers = input("How many salaries do you want to enter?: ")
while x<=numbers:
	salaries = input("Enter the salary number" + str(x) + " : ")

	if(salaries>=100 and salaries<=300):
		salary1 = salary1 + 1
	else:
		salary2 = salary2 + 1
	total = total + salaries
	x=x+1

print("The number of salaries between 100 and 300 are: " + str(salary1))
print("The number of salaries major than 300 are: " + str(salary2))
print("The total of money paid from the company to the employees is: " + str(total))

