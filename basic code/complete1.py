#!/usr/bin/python
#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de multiplos de 15.
#d) El valor acumulado de los numeros ingresados que son pares.

quantity = 10
positive = 0
negative = 0
even = 0
comp = 0
sumatory = 0

for x in range(quantity):
	number = input("Enter the value for the number " + str(x) + ": ")
	if(number >=0):
		positive = positive + 1
	else:
		negative = negative + 1
	if(number %15==0):
		comp = comp + 1
	if(number %2==0):
		even = even + 1
		sumatory = sumatory + number

print("")
print("The quantity of positive numbers is: " + str(positive))
print("The quantity of negative numbers is: " + str(negative))
print("The quantity of numbers compatible with 15 is: " + str(comp))
print("The quantity of even numbers is: " + str(even))
print("The sumatory for all the even numbers is: " + str(sumatory))
print("")




