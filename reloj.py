import tkinter as tk
import time

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Digital")

# Definir el tamaño y el fondo de la ventana
ventana.geometry("400x200")
ventana.config(bg="black")

# Función que actualiza el reloj
def actualizar_reloj():
    # Obtener la hora actual
    hora_actual = time.strftime("%H:%M:%S")
    
    # Mostrar la hora en el label
    label.config(text=hora_actual)
    
    # Actualizar cada 1000 ms (1 segundo)
    ventana.after(1000, actualizar_reloj)

# Crear un label para mostrar la hora
label = tk.Label(ventana, font=("calibri", 40, "bold"), background="black", foreground="white")
label.pack(anchor="center")

# Llamar a la función para actualizar el reloj
actualizar_reloj()

# Ejecutar la ventana principal
ventana.mainloop()
