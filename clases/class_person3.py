#!/usr/bin/python


class Person:
	def Start(self, name, age):
		self.name = name
		self.age = age

	def Calculate(self):
		if self.age >=18:
			print "The person is older than 18 years old"
			print ""
		else:
			print "The person has lower than 18 years old"
			print ""

	def Print(self):
		print ""
		print "--------- Data printed ----------"
		print self.name
		print self.age
		print ""

def main():

	name = raw_input("Enter the person's name: ")
	age = input("Enter the the person's age: ")

	person1 = Person()
	person1.Start(name, age)
	person1.Print()
	person1.Calculate()

if __name__ == '__main__':
	main()