#!/usr/bin/python


def Add_Numbers(number1, number2):
	result = number1 + number2
	print("The result is: " + str(result))

def Substract_Numbers(number1, number2):
	result = number1 - number2
	print("The result is: " + str(result))

def Multiply_Numbers(number1, number2):
	result = number1 * number2
	print("The result is: " + str(result))

def Devide_Numbers(number1, number2):
	result = number1 / number2
	print("The result is: " + str(result))


def main():
	opc = 0
	while True:
		print ""
		print "----------------------------"
		print "[1] ADD TWO NUMBERS         |"
		print "[2] SUBSTRACT TWO NUMBERS   |"
		print "[3] MULTIPLY TWO NUMBERS    |"
		print "[4] DEVIDE TWO NUMBERS      |"
		print "[5] EXIT PROGRAM            |"
		print "----------------------------"
		print ""

		num1 = input("Write the first number: ")
		num2 = input("Write the second number: ")

		opc = input("Please, select an option from the menu: ")

		if opc == 1:
			Add_Numbers(num1,num2)
		elif opc == 2:
			Substract_Numbers(num1,num2)
		elif opc == 3:
			Multiply_Numbers(num1,num2)
		elif opc == 4:
			Devide_Numbers(num1,num2)
		elif opc == 5:
			print "Exit Program....."
			exit(0)
		else:
			print "The option selected does not exist, please select an option from the menu"

if __name__ == '__main__':
	main()