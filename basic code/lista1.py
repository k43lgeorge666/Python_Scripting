#!/usr/bin/python
lista = [10,101,200,3,5,25,300,400,15]
nro_elementos = 0
x = 0
while x<len(lista):
	if lista[x] >100:
		nro_elementos = nro_elementos + 1
	x = x+1
print("La cantidad de elementos mayores a 100 es: " + str(nro_elementos))
print("")

