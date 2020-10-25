#!/usr/bin/python


def Add_Numbers(number1, number2):
	resp = number1 + number2
	print("The result is: " + str(resp))

def Substract_Numbers(number1, number2):
	resp = number1 - number2
	print("The result is: " + str(resp))

def Multiply_Numbers(number1, number2):
	resp = number1 * number2
	print("The result is: " + str(resp))

def Divide_Numbers(number1, number2):
	resp = number1 / number2
	print("The result is: " + str(resp))



def main():

	opc = 0
    while True:

        print ""
        print "-----------------------------"
        print "[1] SUMAR DOS NUMEROS       |"
        print "[2] RESTAR DOS NUMEROS      |"
        print "[3] MULTIPLICAR DOS NUMEROS |"
        print "[4] DIVIDIR DOS NUMEROS     |"
        print "[5] SALIR                   |"
        print "-----------------------------"
        print ""

        num1 = input("Escribe el valor del primer numero: ")
        num2 = input("Escribe el valor del segundo numero: ")

        opc = input("Elije una opcion del menu: ")

        if opc == 1:
            Sumar(num1,num2)
        elif opc == 2:
            Restar(num1, num2)
        elif opc == 3:
            Multiplicar(num1, num2)
        elif opc == 4:
            Dividir(num1, num2)
        elif opc == 5:
            print "Saliendo del programa...."
            exit(0)
        else:
            print "La opcion " + str(opc) +  " no existe, elige otra"


if __name__ == '__main__':
	main()







