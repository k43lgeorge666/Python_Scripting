#!/usr/bin/python

x=1
cont1=0
cont2=0
while x<=10:
	grade = input("Enter a number: ")

	if grade>=7:
		cont1 = cont1+1
	else:
		cont2 = cont2+1

	x=x+1
print("The quantity of numbers major or equal to seven are: " + str(cont1))
print("The quantity of numbers minor than seven are : " + str(cont2))

