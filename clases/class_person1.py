#!/usr/bin/python

class Person:

	def Start(self, name):
		self.value = name

	def Print(self):
		print("Name: ", self.value)


def main():

	person1=Person()
	person1.Start("Peter")
	person1.Print()

	person2=Person()
	person2.Start("Xavier")
	person2.Print()


if __name__ == '__main__':
	main()