#!/usr/bin/python

print ""
print "------------------------------------"
print ""
print "[1] Add two numbers"
print "[2] Substract two numbers"
print "[3] Multiply two numbers"
print "[4] Divide two numbers"
print ""
print "------------------------------------"
print ""

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

opc = input("Enter the an option: ")

if(opc == 1):
	print(number1 + number2)
elif(opc == 2):
	print (number1 - number2)
elif(opc ==3):
	print(number1 * number2)
elif(opc ==4):
	print(number1 / number2)
else:
	print "The selected option does not exist"

