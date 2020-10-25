#!/usr/bin/python
nombres = ["ana", "george", "samuel", "maria", "remberto"]
nro_caracteres = 0
nombres1 = ""
x = 0

while x<len(nombres):
	if len(nombres[x]) >=5:
		nro_caracteres = nro_caracteres + 1
		nombres1 = nombres[x]
	x=x+1
print("")
print("El numero de nombres que tienen 5 o mas caracteres es: " + str(nro_caracteres))
print("LOS nombres de estas personas son: " + nombres1)
print("")