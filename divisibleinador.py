import time

# Bienvenida
print("BIENVENIDO AL DIVISIBLEINADOR")
print("-----------------------------")

time.sleep(1.3)

numero_para_verificar = float(input("Ingrese el numero que quiere dividir: "))
# Espacio para mejorar la lectura
print("---------------------------------------------------------------------")
numero_divisor = float(input("""Ingrese un numero por el cual dividir
para verificar su divisibilidad: """))

time.sleep(2)
print("Procesando...")
time.sleep(0.7)
print("-----------------------------")

# Si es divisible
if numero_para_verificar % numero_divisor == 0:
    print(f"""El numero es divisible.
El resultado de la division es: {numero_para_verificar / numero_divisor}""")

# Si no es divisible
else:
    print(f"""El numero no es divisible su resto es {numero_para_verificar % numero_divisor}
El resultado de la division es de {numero_para_verificar / numero_divisor}""")
