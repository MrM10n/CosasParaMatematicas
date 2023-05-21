"Raizificador"

import math

def raízcuadrada():
    a = float(input("Ingrese el numero: "))
    resultado = math.sqrt(a)
    print(f"El resultado es: {resultado}")

def raízcubica():
    a = float(input("Ingrese su numero: "))
    resultado = math.cbrt(a)
    print(f"El resultado es: {resultado} ")

while True:
    cuborcuad = input("Cual operación desea hacer cub/cua: ")
    if cuborcuad.lower() == "cua":
        raízcuadrada()

    elif cuborcuad.lower() == "cub":
        raízcubica()

    else:
        print("Entrada no valida")

    repetir = input("Quiere realizar otra operación? s/n: ")
    if repetir != "s":
        print("Gracias por usar el raizificador. creado por Mrm10n el 21/05/2023. Un programa dedicado al arte de las matemaricas.")
        break
