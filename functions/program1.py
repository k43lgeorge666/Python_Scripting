#!/usr/bin/python

def add_numbers(number):
	total = 0
	for i in range(0, number):
		element = input("Enter the number: ")
		total = total + element
	print("")
	print("The sumatory for all numbers entered is: " + str(total))
	print("")


def main():
	quantity = input("How many numbers you want to add?: ")
	add_numbers(quantity)


if __name__ == '__main__':
	main()


