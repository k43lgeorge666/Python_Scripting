#!/usr/bin/python

class Operations:

	def Start(self, num1, num2, resp):
		self.num1 = num1
		self.num2 = num2
		self.resp = resp

	def Print(self):
		print("The result is: " + str(self.resp))


	def Add_Numbers(self):
		self.resp = self.num1 + self.num2

	def Substract_Numbers(self):
		self.resp = self.num1 - self.num2

	def Multiply_Numbers(self):
		self.resp = self.num1 * self.num2

	def Divide_Numbers(self):
		self.resp = self.num1 / self.num2

def main():

	opc = 0
	resp = 0

	try:


		while True:

			print ""
			print "-------------------------------"
			print "[1] ADD TWO NUMBERS            |"
			print "[2] SUBSTRACT TWO NUMBERS      |"
			print "[3] MULTIPLY TWO NUMBERS       |"
			print "[4] DIVIDE TWO NUMBERS         |"
			print "[5] EXIT PROGRAM               |"
			print "-------------------------------"
			print ""

			num1 = input("Enter the first number: ")
			num2 = input ("Enter the second number: ")

			opc = input("Enter an option from the menu: ")

			if opc == 1:
				operation1 = Operations()
				operation1.Start(num1,num2,resp)
				operation1.Add_Numbers()
				operation1.Print()

			elif opc == 2:
				operation1 = Operations()
				operation1.Start(num1,num2,resp)
				operation1.Substract_Numbers()
				operation1.Print()

			elif opc == 3:
				operation1 = Operations()
				operation1.Start(num1,num2,resp)
				operation1.Multiply_Numbers()
				operation1.Print()

			elif opc == 4:
				operation1 = Operations()
				operation1.Start(num1,num2,resp)
				operation1.Divide_Numbers()
				operation1.Print()

			elif opc == 5:
				print "Exit Program....."
				print ""
				exit(0)
			else:
				print ""
				print "The option selected does not exist"
				print "Select an option from the menu"
	except:
		print ""
		print "The value provided is incorrect"
		print "Exit Program"
		print ""
		
if __name__ == '__main__':
	main()