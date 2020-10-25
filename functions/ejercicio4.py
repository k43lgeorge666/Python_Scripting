#!/usr/bin/python

def Sumar(numero1, numero2):
    resp = numero1 + numero2
    print "La suma de ambos numeros es: " + str(resp)

def Restar(num1, num2):
    resp = num1 - num2
    print "La resta de ambos numeros es: " + str(resp)

def Multiplicar(valor1, valor2):
    resp = valor1 * valor2
    print "La multiplicacion de ambos numeros es: " + str(resp)

def Dividir(num1, num2):
    resp = num1 / num2
    print "La division de ambos numeros es: " + str(resp)

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

if __name__ == "__main__":
    main()