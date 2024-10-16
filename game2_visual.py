import random
import time
import tkinter as tk
from PIL import Image, ImageTk

# INICIO Visual
root = tk.Tk()
root.title('¡¡ Bienvenido al Juego !!')

# Crear un marco principal
root.geometry("1000x800")

# Crear un marco principal
mainframe = tk.Frame(root)
mainframe.pack(padx=20, pady=20)

# Cargar la imagen y ajustarla
imagen = Image.open("Simon-Game.png")
imagen = imagen.resize((500, 200), Image.Resampling.LANCZOS)  # Redimensionar la imagen al ancho de la ventana
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un Label para mostrar la imagen y centrarla
imagen_label = tk.Label(root, image=imagen_tk)
imagen_label.pack(pady=20)  # Coloca la imagen con espacio hacia abajo

# Título del juego centrado debajo de la imagen
title_label = tk.Label(mainframe, text="Simon dice:", font=("Arial", 24, "bold"))
title_label.pack(pady=20)  # Añadir espacio

# Crear un frame para los botones de colores y alinearlos horizontalmente
colors_frame = tk.Frame(mainframe)
colors_frame.pack(pady=10)


content_frame = tk.Frame(root)
content_frame.pack(pady=10)




# VARIABLES
jugador_seq = []
secuencia = []
buttons = {}
aciertos = 0  # Contador de aciertos
velocidad = 1000  # Velocidad inicial (en milisegundos)
nivel_actual = 1  # Nivel inicial


# Funciones

def start_game():
    global aciertos, velocidad, nivel_actual
    global aciertos
    aciertos = 0  # Reiniciar contador de aciertos
    velocidad = 1000  # Reiniciar la velocidad al iniciar
    nivel_actual = 1  # Nivel inicial
    start_button.pack_forget()  # Ocultar el botón "Start" después de que se presiona
    reset_game()
    next_round()  # Iniciar la primera secuencia

def button_pressed(color):
    jugador_seq.append(color)
    print(f"Secuencia del jugador: {jugador_seq}")
    if len(jugador_seq) == len(secuencia):
        check_sequence()

def mostrar_ganador():
    ganaste_label.pack()
    

def mostrar_perdedor():
    perdiste_label.pack()  # Mostrar la etiqueta de pérdida
    

def mostrar_secuencia(seq):
    for color in seq:
        performance_button(color)

def performance_button(color):
    button = buttons[color]
    button.config(highlightbackground="white", highlightthickness=4)
    root.update()  # Actualizar la ventana
    time.sleep(0.5)  # Pausa
    button.config(highlightbackground="black", highlightthickness=0)
    root.update()
    time.sleep(0.2)  # Pausa breve entre colores

def check_sequence():
    global aciertos, velocidad, nivel_actual
    if jugador_seq == secuencia:
        aciertos += 1  # Incrementar el contador de aciertos
        if aciertos >= 20:
            mostrar_ganador()
            root.after(3000, reset_game)  # Reiniciar juego después de 3 segundos
        else:
            # Aumentar la velocidad del juego en función del número de aciertos
            if aciertos < 7:
                velocidad = 1000  # Nivel 1
                nivel_actual = 1
            elif aciertos < 14:
                velocidad = 700  # Nivel 2
                nivel_actual = 2
            else:
                velocidad = 400 
                nivel_actual = 3 # Nivel 3


            actualizar_nivel()
            root.after(velocidad, next_round)  # Pasar a
    else:
        mostrar_perdedor()
        root.after(3000, reset_game)  # Reiniciar juego después de 2 segundos

def next_round():
    jugador_seq.clear()  # Limpiar la secuencia del jugador
    new_color = random.choice(["Rojo", "Verde", "Azul", "Amarillo"])
    secuencia.append(new_color)
    print(f"Secuencia del juego: {secuencia}")
    root.after(1000, lambda: mostrar_secuencia(secuencia))  # Mostrar la secuencia después de 1 segundo
    ganaste_label.pack_forget()
    perdiste_label.pack_forget()


def actualizar_nivel():
    nivel_label.config(text=f"Nivel actual: {nivel_actual}")  # 

def reset_game():
    global secuencia
    secuencia = []
    jugador_seq.clear()
    ganaste_label.pack_forget()  # Ocultar etiqueta de ganador
    perdiste_label.pack_forget()  # Ocultar etiqueta de pérdida
    
    start_button.pack(pady=20)


# Botones
start_button = tk.Button(mainframe, text="Start", font=("Arial", 16), command=start_game, width=10, height=2)
start_button.pack(pady=30)


# Crear los botones de colores
buttons["Rojo"] = tk.Button(mainframe, text="Rojo", bg="red", command=lambda: button_pressed("Rojo"), width=10, height=5)
buttons["Rojo"].pack(side=tk.LEFT, padx=10, pady=10)

buttons["Verde"] = tk.Button(mainframe, text="Verde", bg="green", command=lambda: button_pressed("Verde"), width=10, height=5)
buttons["Verde"].pack(side=tk.LEFT, padx=10, pady=10)

buttons["Azul"] = tk.Button(mainframe, text="Azul", bg="blue", command=lambda: button_pressed("Azul"), width=10, height=5)
buttons["Azul"].pack(side=tk.LEFT, padx=10, pady=10)

buttons["Amarillo"] = tk.Button(mainframe, text="Amarillo", bg="yellow", command=lambda: button_pressed("Amarillo"), width=10, height=5)
buttons["Amarillo"].pack(side=tk.LEFT, padx=10, pady=10)

# Etiquetas
ganaste_label = tk.Label(mainframe, text="¡Has ganado!", font=("Arial", 24), fg="green")

perdiste_label = tk.Label(mainframe, text="¡Has perdido!", font=("Arial", 24), fg="red")

nivel_label = tk.Label(mainframe, text=f"Nivel actual: {nivel_actual}", font=("Arial", 18))
nivel_label.pack(pady=10)

# Iniciar el loop principal de la aplicación
root.mainloop()
