from tkinter import *
import random


def mostrar_bienvenida():
    menInicio.config(text="Bienvenido jugador")
    root.after(2000, botones_inicio)  # Mostrar los botones después de 2 segundos

def botones_inicio():
    # Solo se mostrarán los botones de inicio y exit una vez que pase el tiempo de bienvenida
    botonInicio.pack()
    botonExit.pack()

def inicio():
    menInicio.config(text="¡preparate! ＼(＾▽＾)／")
    botonInicio.pack_forget()
    botonExit.pack_forget()
    root.after(2000, mostrar_botones)

def mostrar_botones():
    menInicio.config(text="Elige tu arma")
    botonPA.place(x=70, y=225)
    botonPI.place(x=180, y=250)
    botonTI.place(x=270, y=225)



def game1(eleccion):
    objects = ["papel", "tijeras", "piedra"]
    global count, victorias, derrotas, empates, program
    
    #print("***********************************************")
    #print("* Bienvenido jugador, ¡prepárate! ＼(＾▽＾)／ *")
    #print("***********************************************")

    #while count < 3:  # Cambié <= 2 por < 3 para que sean exactamente 3 intentos.
    #    print(f"\nIntento {count + 1}:")  # Mostrar el intento actual.
    #   user = input(emoji.emojize("\nElige tu arma: piedra \U0001F44A, papel \U0001F590 o tijeras: ")).lower()  # Uso de .lower() para hacer la entrada insensible a mayúsculas.

    #   if user not in objects:  # Verifica si la opción del usuario es válida.
    #        print(emoji.emojize("Opción no válida. Vuelve a elegir. \U0001F624"))
    #        continue
        
    program = random.choice(objects)  # Elección aleatoria de la máquina.
    menInicio.config(text=f"Has elegido {eleccion}. La máquina eligió {program}.")

    if program == 'piedra':
        show_enemy('piedra')
    elif program == 'tijeras':
        show_enemy('tijeras')
    else:
        hide_enemy()


    if eleccion == program:
        menInicio.config(text="Empate")
        empates += 1
    elif (eleccion == "papel" and program == "piedra") or \
        (eleccion == "piedra" and program == "tijeras") or \
        (eleccion == "tijeras" and program == "papel"):
        menInicio.config(text="Ganaste")
        victorias += 1
    else:
        menInicio.config(text="Perdiste")
        derrotas += 1
    
    count += 1  # Contar intentos aquí, después de procesar la elección.

    if count >= 3:
        mostrar_resultado_final()

def mostrar_resultado_final():
    hide_enemy()

    if victorias > derrotas and victorias > empates:from tkinter import messagebox 
        menInicio.config(text="\n¡Enhorabuena, ganaste a la máquina, ¡¡¡¡MÀQUINAAAAAAAAAA!!!!(┛｀Д´)┛彡┻━┻ ")
    elif derrotas > victorias and derrotas > empates:
        menInicio.config(text="\nTe ganó una máquina, ¡haztelo mirar! (✧≖‿≖)")
    elif empates > victorias and empates > derrotas:
        menInicio.config(text="\nEmpate total (⊙_☉), intenta de nuevo.")
    else:
        menInicio.config(text="\nNo bebé, otro día será. ღ(U ω Uღ)")

    # Mostrar botones de reinicio y salida
    mostrar_botones_reinicio_salida()

def mostrar_botones_reinicio_salida():

    ocultar_botones_arma()

    botonReinicio = Button(root, text="Reiniciar", command=reinicio, bg="black", fg="white", borderwidth=0)
    botonReinicio.place(x=80, y=150)
    botonSalir = Button(root, text="Salir", command=exit, bg="black", fg="white", borderwidth=0)
    botonSalir.place(x=250, y=150)


def ocultar_botones_arma():
    botonPA.place_forget()
    botonPI.place_forget()
    botonTI.place_forget()

'''
    # Mensajes finales según el resultado
    if count >= 3:
        if victorias > derrotas and victorias > empates:
            menInicio.config(text="\n¡Enhorabuena, ganaste a la máquina, ¡¡¡¡MÀQUINAAAAAAAAAA!!!!(┛｀Д´)┛彡┻━┻ ")
        elif derrotas > victorias and derrotas > empates:
            menInicio.config(text="\nTe ganó una máquina, ¡haztelo mirar! (✧≖‿≖)")
        elif empates > victorias and empates > derrotas:
            menInicio.config(text="\nEmpate total (⊙_☉), intenta de nuevo.")
        else:
            menInicio.config(text="\nNo bebé, otro día será. ღ(U ω Uღ)")

        reinicio()
'''

def show_enemy(tipo):
    global label_enemy
    if tipo == 'piedra':
        enemy_img = PhotoImage(file="Stone.png")
        
    elif tipo == 'tijeras':
        enemy_img = PhotoImage(file="Scissors.png")
       
    label_enemy = Label(root, image=enemy_img, bg='black')
    label_enemy.image = enemy_img
    label_enemy.place(x=175, y=125)

    # Deshabilitar botones
    deshabilitar_botones()

    # Ocultar la imagen después de 2 segundos
    root.after(2000, hide_enemy)

    
def hide_enemy():
    global label_enemy1
    if 'label_enemy' in globals() and label_enemy is not None:
        label_enemy.destroy()  # Oculta la imagen
    

    # Habilitar botones nuevamente
    habilitar_botones()

def deshabilitar_botones():
    botonPA.config(state=DISABLED)
    botonPI.config(state=DISABLED)
    botonTI.config(state=DISABLED)

def habilitar_botones():
    botonPA.config(state=NORMAL)
    botonPI.config(state=NORMAL)
    botonTI.config(state=NORMAL)

def exit():
    root.destroy()

def reinicio():
    global count, victorias, derrotas, empates
    count = 0
    victorias = 0
    derrotas = 0
    empates = 0
    menInicio.config(text="¡Prepárate! ＼(＾▽＾)／")
    
    # Ocultar botones de reinicio y salida si están visibles
    for widget in root.place_slaves():
        if isinstance(widget, Button) and widget['text'] in ["Reiniciar", "Salir"]:
            widget.place_forget()

    # Volver a mostrar los botones de selección de arma
    mostrar_botones()

count = 0
victorias = 0
derrotas = 0
empates = 0
label_enemy = None #Define label_enemy globalmente

root = Tk()
root.title("Menú")
root.geometry("400x300")
root.resizable(False, False)

fondo_imagen = PhotoImage(file="fondogame1.png")
fondo_label = Label(root, image=fondo_imagen)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

menInicio = Label(root, text="", wraplength=300, fg ="white", bg="black")
menInicio.pack(pady=45)

botonInicio = Button(root, text = "Inicio", command=inicio, bg="black", fg="white", borderwidth=0)
botonInicio.pack(pady=10)

botonExit = Button(root, text = "Exit", command=exit, bg="black", fg="white", borderwidth=0)
botonExit.pack(pady=10)

img_piedra = PhotoImage(file="objeto3.png")
botonPI = Button(root, image=img_piedra, command=lambda: game1("piedra"), bg="black", borderwidth=0)

botonPA = Button(root, text = "Papel", command=lambda: game1("papel"), bg="black", fg="white", borderwidth=0)

botonTI = Button(root, text = "Tijeras", command=lambda: game1("tijeras"), bg="black", fg="white", borderwidth=0)

result_label = Label(root, text= "", wraplength=300, bg="black", fg="white", borderwidth=0)
result_label.pack(pady=10)



root.mainloop()

#game1()
#print("\nHas acabado este juego. 凸(｡◕‿◕｡)凸")