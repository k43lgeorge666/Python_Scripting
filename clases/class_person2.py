#!/usr/bin/python

class Student:

	def Start(self, name, grade):
		self.value1 = name
		self.value2 = grade

	def Calculate(self):
		if self.value2 >=4:
			print "The grade is equal or major than 4"
		else:
			print "The grade is lower than 4"

	def Print(self):
		print "Name: " + self.value1
		print "Grade: " + str(self.value2)

def main():
	student1 = Student()

	name = raw_input("Enter the student name: ")
	grade = input("Enter the student grade: ")

	student1.Start(name,grade)
	student1.Calculate()
	student1.Print()

if __name__ == '__main__':
	main()

