#!/usr/bin/python

number = input("Enter the number: ")

if (number >=1 and number%2==0):
	print("the number is a pair positive")
elif(number >=1 and number%2!=0):
	print("The number is impair and is positive")
elif(number <=1 and number%2==0):
	print("The number is pair negative")
elif(number <=1 and number%2!=0):
	print("The number is impair negative")
elif(number == 0):
	print("the number is zero")
else:
	print("The number cannot be determined!")



