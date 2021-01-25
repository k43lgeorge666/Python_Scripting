#!/usr/bin/python

class Operations:
	def __init__(self, number1, number2):
		
		self.number1 = number1
		self.number2 = number2

	def Add_numbers(self):
		result = self.number1 + self.number2
		print("The result is: " + str(result))

	def Substract_numbers(self):
		result = self.number1 - self.number2
		print("The result is: " + str(result))

	def Multiply_numbers(self):
		result = self.number1 * self.number2
		print("The result is: " + str(result))

	def Divide_numbers(self):
		result = self.number1 / self.number2
		print("The result is: " + str(result))

def main():
	print ""
	n1 = input("Enter the first number: ")
	n2 = input ("Enter the second number: ")

	opc = Operations(n1,n2)
	opc.Add_numbers()
	opc.Substract_numbers()
	opc.Multiply_numbers()
	opc.Divide_numbers()

if __name__ == '__main__':
	main()