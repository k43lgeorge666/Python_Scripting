#!/usr/bin/python

#numbers major than 1000

quantity = 0
major = 0
minor = 0
number = input("How many numbers do you want to enter?: ")
for x in range(number):
	value = input("Enter the value number " + str(x) + ": ")
	if(value>1000):
		major = major + 1
	else:
		minor = minor + 1

print("")
print("The quantity of numbers major than 1000 are: " + str(major))
print("The auqntity of numbers minor than 1000 are: " + str(minor))
print("")

