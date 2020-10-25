#!/usr/bin/python

#height average

x=1
total = 0
numbers = input("How many numbers do you want to provide?: ")
while x<=numbers:
	data = float (input("Enter the number " + str(x) + " : "))
	total = total + data
	x=x+1

average = total / numbers
print("The height average is: " + str(average))






