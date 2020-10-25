#!/usr/bin/python
list1=[]
list2=[]

total1 = 0
total2 = 0

print("")
quantity1 = input ("How many employees are there in the morning?: ")
quantity2 = input("HOw many employees are there in the afternoon?: ")

print("")
for i in range(quantity1):
	morning = float(input("Enter the salary number " + str(i) +  " for the morning employee(s): "))
	list1.append(morning)
	total1 = total1 + morning

print("")
for x in range(quantity2):
	afternoon = float(input("Enter the salary number " + str(x) +  " for the afternoon employee(s): "))
	list2.append(afternoon)
	total2 = total2 + afternoon

print("")
print("--------- The Salaries for the morning employees ----------")
print("")
print(str(list1))

print("")
print("--------- The Salaries for the afternoon employees ----------")
print("")
print(str(list2))


print("")
print("The total of the salaries for the morning employees is: " + str(total1))
print("The total of the salaries for the afternoon employees is: " + str(total2))
print("")





