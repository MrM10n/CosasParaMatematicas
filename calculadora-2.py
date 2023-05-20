"""CALCULADORA_2"""
#Suma
def suma():
    num = int(input("Ingrese el numero: "))
    num2 = int(input("Ingrese la cantidad que aumentará: "))

    print(num + num2)
#Resta
def resta():
    num = int(input("Ingrese el numero: "))
    num2 = int(input("Ingrese la cantidad que le restará: "))

    print(num - num2)
#Divide
def division():
    num = int(input("Ingrese el numero: "))
    num2 = int(input("Ingrese por cuanto lo dividirá: "))

    print(num / num2)
#Multiplica
def multiplicacion():
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese por cuanto lo multiplicará: "))

    print(num * num2)

def elevar():
    num = int(input("Ingrese el numero que desea elevar: "))
    num2 = int(input("A cuanto lo elevará: "))
    print (num ** num2)


def divbaja():
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese la cantidad por la cual se hara la división baja: "))

    print(num // num2)

def resto():
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el numero por el cual se dividira para conseguir el resto: "))

    resultado = num % num2

    print(resultado)
    if resultado == 0:
        print("Los numeros son divisibles")

while True:
    operacion = input("""Que operación desea hacer
(suma/resta/multiplicación/división/elevar/resto/división baja): """)

    if operacion.lower() == "suma":
        suma()

    elif operacion.lower() == "resta":
        resta()

    elif operacion.lower() == "multiplicación":
        multiplicacion()

    elif operacion.lower() == "división":
        division()

    elif operacion.lower() == "elevar":
        elevar()

    elif operacion.lower() == "división baja":
        divbaja()

    elif operacion.lower() == "resto":
        resto()

    else:
        print("Entrada no valida")


    repetir = input("¿Desea realizar otra operación? (s/n): ")
    if repetir.lower() != "s":
        print("""Gracias por usar la calculadora ver:2 creada por Mrm10n el 20/05/2023.
        Un programa hecho para el arte de las matematicas.""")
        break
