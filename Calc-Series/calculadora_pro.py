"Calculadora pero esta vez trae botones"
#pylint: disable=C0301
#pylint: disable=W
import tkinter as tk

# Configuración de la ventana
Ventana = tk.Tk()
Ventana.title("Calculadora")

# Interior de la ventana
# Caja de texto
caja = tk.Entry(Ventana, font="Consolas")
# Fila 0, Columna 0 para decir que es el primer objeto
caja.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

i = 0

# Funciones
def click_boton(valor):
    "Inserta el valor que le es proporcionado a cada boton"
    global i
    caja.insert(i, valor)
    i += 1
def borrar():
    "Borra lo escrito en la caja"
    caja.delete(0, tk.END)
    i = 0

def hacer_ecuacion():
    "Hace las ecuaciones que le proporcionas"
    ecuacion = caja.get()
    result = eval(ecuacion)
    caja.delete(0, tk.END)
    caja.insert(0, result)
    i = 0
#Botones
boton1 = tk.Button(Ventana, text = "1", width = 5, height = 2,command= lambda: click_boton(1))
boton2 = tk.Button(Ventana, text = "2", width = 5, height = 2,command= lambda: click_boton(2))
boton3 = tk.Button(Ventana, text = "3", width = 5, height = 2,command= lambda: click_boton(3))
boton4 = tk.Button(Ventana, text = "4", width = 5, height = 2,command= lambda: click_boton(4))
boton5 = tk.Button(Ventana, text = "5", width = 5, height = 2,command= lambda: click_boton(5))
boton6 = tk.Button(Ventana, text = "6", width = 5, height = 2,command= lambda: click_boton(6))
boton7 = tk.Button(Ventana, text = "7", width = 5, height = 2,command= lambda: click_boton(7))
boton8 = tk.Button(Ventana, text = "8", width = 5, height = 2,command= lambda: click_boton(8))
boton9 = tk.Button(Ventana, text = "9", width = 5, height = 2,command= lambda: click_boton(9))
boton0 = tk.Button(Ventana, text = "0", width = 13, height = 2,command= lambda: click_boton(0))

boton_borrar = tk.Button(Ventana, text = "AC", width = 5, height = 2,command=lambda: borrar())
boton_parentesis1 = tk.Button(Ventana, text = "(", width = 5, height = 2,command= lambda: click_boton("("))
boton_parentesis2 = tk.Button(Ventana, text = ")", width = 5, height = 2,command= lambda: click_boton(")"))
boton_punto = tk.Button(Ventana, text = ".", width = 5, height = 2,command= lambda: click_boton("."))


boton_div = tk.Button(Ventana, text = "/", width = 5, height = 2,command= lambda: click_boton("/"))
boton_mult = tk.Button(Ventana, text = "x", width = 5, height = 2,command= lambda: click_boton("*"))
boton_rest = tk.Button(Ventana, text = "-", width = 5, height = 2,command= lambda: click_boton("-"))
boton_igual = tk.Button(Ventana, text = "=", width = 5, height = 2,command= lambda: hacer_ecuacion())
boton_sum = tk.Button(Ventana, text = "+", width = 5, height = 2,command= lambda: click_boton("+"))







# Agregar botones a la pantalla
boton_borrar.grid(row =1, column =0, padx = 5, pady = 5)
boton_parentesis1.grid(row =1, column =1, padx = 5, pady = 5)
boton_parentesis2.grid(row =1, column =2, padx = 5, pady = 5)
boton_div.grid(row =1, column =3, padx = 5, pady = 5)

boton7.grid(row =2, column =0, padx = 5, pady = 5)
boton8.grid(row =2, column =1, padx = 5, pady = 5)
boton9.grid(row =2, column =2, padx = 5, pady = 5)
boton_mult.grid(row =2, column =3, padx = 5, pady = 5)

boton4.grid(row =3, column =0, padx = 5, pady = 5)
boton5.grid(row =3, column =1, padx = 5, pady = 5)
boton6.grid(row =3, column =2, padx = 5, pady = 5)
boton_rest.grid(row =3, column =3, padx = 5, pady = 5)

boton1.grid(row =4, column =0, padx = 5, pady = 5)
boton2.grid(row =4, column =1, padx = 5, pady = 5)
boton3.grid(row =4, column =2, padx = 5, pady = 5)
boton_sum.grid(row =4, column =3, padx = 5, pady = 5)

boton0.grid(row =5, column =0, columnspan=2, padx = 5, pady = 5)
boton_punto.grid(row =5, column =2, padx = 5, pady = 5)
boton_igual.grid(row =5, column =3, padx = 5, pady = 5)



Ventana.mainloop()
