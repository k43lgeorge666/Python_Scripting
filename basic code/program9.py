#!/usr/bin/python

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
number3 = input("Enter the third number: ")

if(number1 > number2 and number1 > number3):
	print("The major number is: " + str(number1))
elif(number2 > number1 and number2 > number3):
		print("The major number is: " + str(number2))
elif(number3 > number1 and number3 > number2):
		print("The major number is: " + str(number3))
else:
	print ("Cannot be determined!")
