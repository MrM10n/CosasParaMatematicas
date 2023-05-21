"radiador.py"
import math 

def perimetro():
    diametro = float(input("Ingrese el diametro de la circunferencia: "))

    perimetrototal = diametro * math.pi
    print(f"El perimetro del circulo es de {perimetrototal}")

def area():
    radio = float(input("Ingrese el radio de la circunferencia: "))

    areatotal = math.pi * radio ** 2
    print(f"El area del circulo es de {areatotal}")
while True:
    areaoperi = input("Desea coneguir el area o el perimetro? p/a: ")
    if areaoperi == "p":
        perimetro()
    elif areaoperi == "a":
        area()
    else:
        print("Entrada no valida")

    reiniciar = input("Desea realizar un calculo de nuevo? s/n: ")
    if reiniciar != "s":
        print("Gracias por usar el radiador hecho por Mrm10n el 21/05/2023")
        break
