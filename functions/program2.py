#!/usr/bin/python

def multiply_table(element):
	print("")
	for i in range(1,11):
		total = element * i
		print(str(element) + " * " + str(i) + " = " + str(total))
	print("")	 

def main():
	number = input("Enter the number to list the table for: ")
	multiply_table(number)


if __name__ == '__main__':
	main()