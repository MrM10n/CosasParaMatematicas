#Mrm10n
#12/05/2023
#Programa creado para el arte de las matematicas

# Bienvenida
print("""BIENVENIDO A EL CUBICUADRIFICADOR""")
print("----------------------------------")

# Pregunta el tipo de dato que se usará
floatorint = input("Usaras un dato float o int f/i: ")

# En caso de que sea float
if floatorint == "f":
    i = float(input("Ingrese un numero flotante: "))
    print(f"Su numero fue {i}")
    print("----------------------")
    print(f"Al cuadrado sería {i * i}")
    print("----------------------")
    print(f"Al cubo seria {i * i * i}")
    print("----------------------")
    print("Gracias por usar el cubicuadrificador")
    print("----------------------")

# En caso de que sea int
elif floatorint == "i":
    i = int(input("Ingrese un numero entero: "))
    print(f"Su numero fue {i}")
    print("----------------------")
    print(f"Al cuadrado sería {i * i}")
    print("----------------------")
    print(f"Al cubo seria {i * i * i}")
    print("----------------------")
    print("Gracias por usar el cubicuadrificador")
    print("----------------------")

# Si la opcion no es valida
else:
    print("Esa opcion no es valida")
