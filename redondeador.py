import time

# Bienvenida
print("BIENVENIDO AL REDONDEADOR")
print("--------------------------")
print("                           ")

# Pregunta si el dato será un dato entero o flotante
floatorint = input("Será float o int f/i help para mas informacion:  ")

# Si es entero
if floatorint == "i":
    # Bienvenida a los numeros enteros
    print("Ha seleccionado numeros enteros")
    print("--------------------------------")
    # Tiempo que tarda en decir "----------------------" y preguntar el numero
    time.sleep(1.5)
    numared = int(input("Deme un numero entero para redondear: ")) # Numero para redondear
    redondeo = int(input("A cuanto lo va a redondear: ")) # Cifras a redondear

    # Se redondea
    numeroredondo = (numared // 10**redondeo) * 10**redondeo
    print(f"Su numero redondeado es {numeroredondo}!") # Respuesta

# Si es flotante
elif floatorint == "f":
    # Bienvenida a los numeros flotantes
    print("Ha seleccionado numeros flotantes")
    print("--------------------------------")
    # Tiempo que tarda en decir "----------------------" y preguntar el numero
    time.sleep(1.5)
    numared = float(input("Deme un numero con decimal para redondear: ")) # Numero para redondear
    redondeo = int(input("A cuanto lo va a redondear (enteros): ")) # Cifras a redondear

    # Se redondea
    numeroredondo = round(numared, redondeo)
    print(f"Su numero redondeado es {numeroredondo}!") # Respuesta


# Para el help
elif floatorint == "help":
    print("""Este programa fue creado por Mrm10n el 11/05/2023.
    Con la intencion de ayudar al redondeo. Gracias por usar redondeador.""") # Metadatos y agradecimientos

# Entradas no validas
else:
    print("Entrada no valida")
