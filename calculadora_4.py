"Calculadora 4"
import math

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

def pitagoras():
    a = int(input("Ingrese el primer cateto: "))
    b = int(input("Ingrese el segundo cateto: "))

    c = a**2 + b**2

    print(f"La hipotenusa equivale a: {c}")

def secuencia():
    a = int(input("Inserte el primer termino: ")) # Primer termino
    n = int(input("Inserte el numero de termino que necesitas: ")) # El numero de termino
    d = int(input("Inserte la diferencia común: ")) # Diferencia común

    resultado = d * (n-1) + a
    print(f"El termino que solicitó fué: {resultado}")
    print(f"La formula fué: {resultado} = {d}({n} - 1) + {a} ") # Formula

def IMC():
    peso = float(input("Ingrese su peso (en kilogramos): "))
    estatura = float(input("Ingrese su altura (en metros): "))
    InMaCor = peso / (estatura * estatura)
    print(f"Su IMC es de {InMaCor}")

def redondear():
    numared = float(input("Deme un numero con decimal para redondear: ")) # Numero para redondear
    redondeo = int(input("A cuanto lo va a redondear (enteros): ")) # Cifras a redondear

    # Se redondea
    numeroredondo = round(numared, redondeo)
    print(f"Su numero redondeado es {numeroredondo}") # Respuesta

def raízcubica():
    a = float(input("Ingrese su numero: "))
    resultado = math.cbrt(a)
    print(f"El resultado es: {resultado} ")

def raízcuadrada():
    a = float(input("Ingrese el numero: "))
    resultado = math.sqrt(a)
    print(f"El resultado es: {resultado}")


while True:
    operacion = input("""Que operación desea hacer
(suma/resta/multiplicación/división/elevar/resto/división baja/
Indice de masa corporal "IMC"/Secuencia/
Teorema de Pitagoras/Redondeo/Raíz cubica/Raíz cuadrada): """)

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

    elif operacion.lower() == "imc":
        IMC()

    elif operacion.lower() == "secuencia":
        secuencia()

    elif operacion.lower() == "teorema de pitagoras":
        pitagoras()

    elif operacion.lower() == "redondeo":
        redondear()

    elif operacion.lower() == "raíz cuadrada":
        raízcuadrada()

    elif operacion.lower() == "raíz cubica":
        raízcubica()

    else:
        print("Entrada no valida")


    repetir = input("¿Desea realizar otra operación? (s/n): ")
    if repetir.lower() != "s":
        print("""Gracias por usar la calculadora ver:4 creada por Mrm10n el 20/05/2023.
        Un programa hecho para el arte de las matematicas.""")
        break
