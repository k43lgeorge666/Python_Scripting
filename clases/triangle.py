#!/usr/bin/python

class Triangle:
	def Start(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def Higher_Side(self):
		if self.side1 > self.side2 and self.side1 > self.side3:
			print ""
			print "The higher side is: " + str(self.side1)

		elif self.side2 > self.side1 and self.side2 > self.side3:
			print ""
			print "The higher side is: " + str(self.side2)

		elif self.side1 == self.side2 and self.side1 == self.side3:
			print ""
			print "The three sides are equal" 
		else:
			print ""
			print "The higher side is: " + str(self.side3)

	def Print(self):
		print ""
		print "--------- The sides of the triangle -----------"
		print ""
		print str(self.side1)
		print str(self.side2)
		print str(self.side3)

	def Equilateral(self):

		if self.side1 == self.side2 and self.side1 == self.side3:
			print ""
			print "The triangle is Equilateral"
			print ""
		else:
			print ""
			print "The triangle is not Equilateral"
			print ""


def main():

	print ""

	side1 = input("Enter the first side of the triangle: ")
	side2 = input("Enter the second side of the triangle: ")
	side3 = input("Enter the third side of the triangle: ")

	triangle1 = Triangle()
	triangle1.Start(side1, side2, side3)
	triangle1.Print()
	triangle1.Higher_Side()
	triangle1.Equilateral()

if __name__ == '__main__':
	main()