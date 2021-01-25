#!/usr/bin/python

class Carro(object):
	def __init__(self):
		self.color = "Rojo"
		self.puertas = 4
		self.tipo = "Deportivo"

	def Movilidad(self):
		print ("Este es el metodo movilidad")


def main():
	auto = Carro()
	auto.Movilidad()


if __name__ == '__main__':
	main()

