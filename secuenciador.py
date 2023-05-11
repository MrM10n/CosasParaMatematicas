import time

# Bienvenida
print("BIENVENIDO AL SECUENCIADOR")
time.sleep(0.7)
print("---------------------------")

# Informacion o continuar con el programa
Info = input("Info para mas información, no escribas nada para continuar: ")
if Info == "":

    a = int(input("Inserte el primer termino: ")) # Primer termino
    n = int(input("Inserte el numero de termino que necesitas: ")) # El numero de termino
    d = int(input("Inserte la diferencia común: ")) # Diferencia común

    resultado = d * (n-1) + a

    print("Procesando...")
    time.sleep(0.7)

    # Resultado
    print(f"El primer termino fué {a}, su diferencia común fué {d}, el numero de temino que solicito fué {n} y el resultado fué: {resultado}") 
    print("---------------------------------------")
    time.sleep(0.5)
    print("Sacando formula...")
    time.sleep(2)
    print(f"La formula fué: {resultado} = {d}({n} - 1) + {a} ") # Formula

elif Info == "info":
    print("SECUENCIADOR, por Mrm10n, 11/05/2023, creado para las secuencias matematicas. an = d(n-1) + a1") # Informacion "info"

elif Info == "Info":
    print("SECUENCIADOR, por Mrm10n, 11/05/2023, creado para las secuencias matematicas. an = d(n-1) + a1") # Informacion "Info"

else:
    print("Entrada no valida") # Entradas no validas