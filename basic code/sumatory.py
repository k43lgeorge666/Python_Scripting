#!/usr/bin/python

quantity = 10
result = 0
for x in range(quantity):
	number = input("Enter the value for the number " + str(x) + ": ")
	if(x>4):
		result = result + number

print("The sumatory for the last 5 numbers is: " + str(result))
print("")



