#!/usr/bin/python

#classmethod
#staticmethod
#property

class prueba(object):
	def __init__(self, radio):
		self.radio = radio

	#nos ayuda a usar una funcion sin que antes sea atribuida a un objeto
	@classmethod 
	def saludo(cls, nombre):
		print "hola " + nombre

	#podemos llamar a la funcion desde main sin mandar argumentos de la clase
	@staticmethod
	def saludo_static():
		print "Bienvenido"

	#@property
	def area_circulo(self):
		return 3.1416*(self.radio**2)


def main():
	#prueba.saludo("Hacker")
	c = prueba(5)
	#c.saludo_static()
	area = c.area_circulo
	print(area)

if __name__ == '__main__':
	main()




