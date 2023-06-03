"Calculadora 5"
import math
def aritmetica():
#Suma
    def suma():
        "Suma"
    num = int(input("Ingrese el numero: "))
    num2 = int(input("Ingrese la cantidad que aumentará: "))

    print(num + num2)
    #Resta
    def resta():
        "Resta"
        num = int(input("Ingrese el numero: "))
        num2 = int(input("Ingrese la cantidad que le restará: "))

        print(num - num2)
    #Divide
    def division():
        "Division"
        num = int(input("Ingrese el numero: "))
        num2 = int(input("Ingrese por cuanto lo dividirá: "))

        print(num / num2)
    #Multiplica
    def multiplicacion():
        "Multiplicacion"
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese por cuanto lo multiplicará: "))

    print(num * num2)

    eleccion = input("Bienvenido a aritmetica basica, desea multiplicar, sumar, dividir o restar")
    if eleccion.lower == "sumar":
        suma()
    elif eleccion.lower == "multiplicar":
        multiplicacion()
    elif eleccion.lower == "dividir":
        division()
    elif eleccion == "restar":
        resta()


def elevar():
    "Elevar"
    num = int(input("Ingrese el numero que desea elevar: "))
    num2 = int(input("A cuanto lo elevará: "))
    print (num ** num2)


def divbaja():
    "Division baja"
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese la cantidad por la cual se hara la división baja: "))

    print(num // num2)

def resto():
    "Resto"
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el numero por el cual se dividira para conseguir el resto: "))

    resultado = num % num2

    print(resultado)
    if resultado == 0:
        print("Los numeros son divisibles")

def pitagoras():
    "Pitagoras"
    catetoa = int(input("Ingrese el primer cateto: "))
    catetob = int(input("Ingrese el segundo cateto: "))

    hipotenusa = catetoa**2 + catetob**2

    print(f"La hipotenusa equivale a: {hipotenusa}")

def secuencia():
    "Secuencias"
    primer_termino = int(input("Inserte el primer termino: ")) # Primer termino
    #Numero de termino
    numero_de_termino = int(input("Inserte el numero de termino que necesitas: "))
    diferencia_comun = int(input("Inserte la diferencia común: ")) # Diferencia común

    resultado = diferencia_comun * (numero_de_termino-1) + primer_termino
    print(f"El termino que solicitó fué: {resultado}")
    print(f"""La formula fué:
          {resultado} = {diferencia_comun}({numero_de_termino} - 1) + {primer_termino}""") # Formula

def indice_de_masa_corporal():
    "Calcula el IMC"
    peso = float(input("Ingrese su peso (en kilogramos): "))
    estatura = float(input("Ingrese su altura (en metros): "))
    in_ma_cor = peso / (estatura * estatura)
    print(f"Su IMC es de {in_ma_cor}")

def redondear():
    "Redondea numeros de tipo float"
    numared = float(input("Deme un numero con decimal para redondear: ")) # Numero para redondear
    redondeo = int(input("A cuanto lo va a redondear (enteros): ")) # Cifras a redondear

    # Se redondea
    numeroredondo = round(numared, redondeo)
    print(f"Su numero redondeado es {numeroredondo}") # Respuesta

def raizcubica():
    "Raices cubicas"
    num = float(input("Ingrese su numero: "))
    resultado = math.cbrt(num)
    print(f"El resultado es: {resultado} ")

def raizcuadrada():
    "Raices cuadradas"
    num = float(input("Ingrese el numero: "))
    resultado = math.sqrt(num)
    print(f"El resultado es: {resultado}")

def perimetro():
    "Perimetro de un circulo"
    diametro = float(input("Ingrese el diametro de la circunferencia: "))

    perimetrototal = diametro * math.pi
    print(f"El perimetro del circulo es de {perimetrototal}")

def area():
    "Area de un circulo"
    radio = float(input("Ingrese el radio de la circunferencia: "))

    areatotal = math.pi * radio ** 2
    print(f"El area del circulo es de {areatotal}")

def sysnum():
    "Sistemas numericos"

    def octa():
        "Convierte numeros en octal"

        num = int(input("Ingresa el numero entero que deseas convertir: "))
        print(f"El numero que ingreso sería: {oct(num)} en el sistema octal.")

    def hexa():
        "Convierte numeros en hexadecimal"

        num = int(input("Ingresa el numero entero que deseas convertir: "))
        print(f"El numero que ingreso sería: {hex(num)} en el hexadecimal.")

    def bina():
        "Convierte numeros en binario"

        num = int(input("Ingresa el numero entero que deseas convertir: "))
        print(f"El numero que ingreso sería: {bin(num)} en binario.")

    eleccion = input("Qué sistema numerico deseas usar octal, hexadecimal o binario bin/hex/oct: ")
    if eleccion.lower == "bin":
        bina()

    elif eleccion.lower == "oct":
        octa()

    elif eleccion.lower == "hex":
        hexa()



while True:
    operacion = input("""Que operación desea hacer
(aritmetica básica/elevar/resto/división baja/
Indice de masa corporal "IMC"/Secuencia/
Teorema de Pitagoras/Redondeo/Raíz cubica/Raíz cuadrada/
Area de un circulo/Perimetro del circulo/Sistemas Numericos): """)

    if operacion.lower() == "aritmetica básica":
        aritmetica()

    elif operacion.lower() == "elevar":
        elevar()

    elif operacion.lower() == "división baja":
        divbaja()

    elif operacion.lower() == "resto":
        resto()

    elif operacion.lower() == "imc":
        indice_de_masa_corporal()

    elif operacion.lower() == "secuencia":
        secuencia()

    elif operacion.lower() == "teorema de pitagoras":
        pitagoras()

    elif operacion.lower() == "redondeo":
        redondear()

    elif operacion.lower() == "raíz cuadrada":
        raizcuadrada()

    elif operacion.lower() == "raíz cubica":
        raizcubica()

    elif operacion.lower() == "area de un circulo":
        area()

    elif operacion.lower() == "perimetro del circulo":
        perimetro()

    elif operacion.lower() == "sistemas numericos":
        sysnum()

    else:
        print("Entrada no valida")


    repetir = input("¿Desea realizar otra operación? (s/n): ")
    if repetir.lower() != "s":
        print("""Gracias por usar la calculadora ver:6 creada por Mrm10n el 3/06/2023.
        Un programa hecho para el arte de las matematicas.""")
        break
