#!/usr/bin/python

number = input("Enter the number: ")

if(number >=0 and number <10):
	print("The number has one digit only")
if(number >=10 and number <100):
	print("The number has two digits")
if(number >=100 and number <1000):
	print("The number has three digits")
else:
	print("Error, the number entered has more digits")
	
	
