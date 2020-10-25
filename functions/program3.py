#!/usr/bin/python


def multiply_table(element):
	cont = 1
	total = 0
	print("")
	while cont<=10:
		total = element * cont
		print(str(element) + " * " + str(cont) + " = " + str(total))
		cont = cont + 1
	print("")

def main():
	number = input("Enter the number to display the table for: ")
	multiply_table(number)


if __name__ == '__main__':
	main()