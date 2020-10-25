#!/usr/bin/python

#verify the quantity of even numbers entered

x=1
even=0
odd=0
total = 0
quantity = input("How many numbers do you want to enter?: ")
while x<=quantity:
	number = input("Enter the number " + str(x) + ": ")
	if(number %2==0):
		even = even + 1
	else:
		odd = odd + 1
	total = total + number
	x=x+1

print("")
print("The quantity of even numbers is: " + str(even))
print("The quantity of odd numbers is: " + str(odd))
print("The sumatory for all numbers is: " + str(total))
print("")

