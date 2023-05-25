"Volumenificador"

import math

def matcubo():
    def area():
        a = int(input("Ingresa la longitud de un lado: "))
        total = ((a**2)*6)
        print(f"El resultado es: {total}")

    def volumen():
        a = int(input("Ingrese la longitud de una arista: "))
        total = a**3
        print(f"El resultado es: {total}")


    elegir = input("Volumen o area? a/v: ")
    if elegir.lower() == "a":
        area()
    elif elegir.lower() == "v":
        volumen()

def matesfera():
    def area():
        r = int(input("Ingrese el radio de la esfera: "))
        total = 4*math.pi*r**2
        print(f"El resultado es: {total}")

    def volumen():
        r = int(input("Ingrese el radio de la esfera: "))
        total = (4/3) * math.pi * r ** 3
        print(f"El resultado es: {total}")
        
    elegir = input("Volumen o area? a/v: ")
    if elegir.lower() == "a":
        area()
    elif elegir.lower() == "v":
        volumen()

def matcilindro():
    def volumen():
        r = int(input("Ingrese el radio de las bases: "))
        h = int(input("Ingrese la altura del cilindro: "))
        total = math.pi * r**2 * h
        print(f" El resultado es {total}")

    def area():
        r = int(input("Ingrese el radio de las bases: "))
        h = int(input("Ingrese la altura del cilindro: "))
        total = 2 * math.pi * r * (r + h)
        print(f"El resultado es: {total}")

    elegir = input("Volumen o area? a/v: ")
    if elegir.lower() == "a":
        area()
    elif elegir.lower() == "v":
        volumen()

while True:
    eleccion = input("Que operación desea hacer cubo/cilindro/esfera")
    if eleccion.lower() == "cubo":
        matcubo()

    elif eleccion.lower() == "cilindro":
        matcilindro()

    elif eleccion.lower() == "esfera":
        matesfera()

    else:
        print("Entrada no valida")

        repetir = input("Desea hacer otra operación s/n: ")
        if repetir != "s":
            print("Gracias por usar el volumenificador creado por Mrm10n el 25/05/2023")
            break
