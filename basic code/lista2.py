#!/usr/bin/python
lista = [10,5,3,43,50,7]
nro_elementos = 0
x = 0
while x<len(lista):
	if lista[x] >=7:
		nro_elementos = nro_elementos + 1
	x = x+1
print("La cantidad de elementos mayores a 7 es: " + str(nro_elementos))
print("")

