#!/usr/bin/python

list1=[]
taller = 0 
smaller = 0
total = 0

quantity = input("How many person's height you want to enter?: ")
for i in range(quantity):
	height = float(input("Enter the height for the person number: " + str(i) + ": "))
	list1.append(height)
	total = total + height / quantity

	if height >= total:
		taller = taller + 1
	else:
		smaller = smaller + 1
print("")
print("-------- The list of the heights stored -----")
print(str(list1))
print("")
print("-------- The Average for the heights stored --------")
print("")
print(str(total))
print("")
print("-------- The quantity of heights higher than the Average --------- ")
print("")
print(str(taller))
print("")
print("-------- The quantity of heights lower than the Average --------- ")
print("")
print(str(smaller))




