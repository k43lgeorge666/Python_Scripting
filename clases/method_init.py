#!/usr/bin/python

class Operations:

	def __init__(self):
		print ""
		self.num1=input("Enter the first value: ")
		self.num2=input("Enter the second value: ")
		self.Menu()

	def Menu(self):

		try:

			while True:
				print ""
				print "----------- MAIN MENU ----------"
				print "                                |"
				print "[1] Add two numbers             |"
				print "[2] Substract two numbers       |"
				print "[3] Multiply two numbers        |"
				print "[4] Divide two numbers          |"
				print "[5] Exit Program                |"
				print "                                |"
				print "--------------------------------"
				print ""

				opc = input ("Select an option from the menu: ")

				if opc == 1:
					self.Add_Numbers()
				elif opc == 2:
					self.Substract_Numbers()
				elif opc == 3:
					self.Multiply_Numbers()
				elif opc == 4:
					self.Divide_Numbers()
				elif opc == 5:
					print ""
					print "Exit Program"
					exit(0)
					print ""
				else:
					print ""
					print "The option selected does no exist"
					print "Type an option from the menu"

		except:
			print ""
			print "The selectec option is incorrect"
			print "Exit Program"
			print ""

	def Add_Numbers(self):
		print ""
		add = self.num1 + self.num2
		print "The result is: " + str(add)

	def Substract_Numbers(self):
		print ""
		substract = self.num1 - self.num2
		print "The result is: " + str(substract)

	def Multiply_Numbers(self):
		print ""
		multiply = self.num1 * self.num2
		print "The result is: " + str(multiply)

	def Divide_Numbers(self):
		print ""
		divide = self.num1 + self.num2
		print "The result is: " + str(divide)

#Main Block

operation1 = Operations()





