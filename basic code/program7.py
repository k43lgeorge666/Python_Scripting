#!/usr/bin/python

number1 = input("Enter the first grade: ")
number2 = input("Enter the second grade: ")
number3 = input("Enter the third grade: ")

result = number1 + number2 + number3

if (result >=7):
	print("Approved")
elif (result >=4 and result<7):
	print("Regular")
elif (result <4):
	print("Failed")

