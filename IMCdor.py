import time

# Binvenida
print("BIENVENIDO AL IMCDOR")
print("---------------------")
time.sleep(2)

peso = float(input("Ingrese su peso (en kilogramos): "))

estatura = float(input("Ingrese su altura (en metros): "))

# Calculando
time.sleep(2)
print("Calculando IMC [|   ]")
time.sleep(2)
print("Calculando IMC [||   ]")
time.sleep(2)
print("Calculando IMC [|||  ]")
time.sleep(2)
print("Calculando IMC [|||| ]")
time.sleep(2)
print("Calculando IMC [|||||]")

# Formula del ICM y la respuesta
InMaCor = peso / (estatura * estatura)
print(f"Su indice de masa corporal es {InMaCor}")
print("-------------------------------")
time.sleep(2)
print("Clasificando su IMC")
time.sleep(2)
print("-------------------------------")

# Tipos de masas corporales
if InMaCor <= 18.5:
    print("Su masa corporal es baja")
elif InMaCor > 18.5:
    print("Su masa corporal es normal")
elif InMaCor > 24.9:
    print("Usted padece de sobrepeso")
elif InMaCor > 29.9:
    print("Usted padece de obesidad grado I")
elif InMaCor >  34.9:
    print("Usted padece de obecidad grado II")
elif InMaCor > 39.9:
    print("Usted padece de obesidad grado III (obesidad mórbida)")
