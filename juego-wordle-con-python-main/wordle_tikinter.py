import tkinter as tk
import random

# Definición de pools de palabras
palabras = [
    "actor", "busca", "curar", "dagas", "error", 
    "finca", "ganas", "hacer", "islas", "jefas", 
    "moler", "nadar", "obras", "pedir", "quedo", 
    "redes", "sonar", "tabla", "verde", "yogur", 
    "zorro"
]

pool2 = [
    "perro", "gatos", "medio", "melon", "meter", 
    "metro", "casas", "flora", "cisne", "citas", 
    "clara", "abeto", "aguas", "agudo", "luces", 
    "mujer", "coche", "silla", "mesas", "jugar", 
    "cielo", "piano", "sabor", "salud", "pasar", 
    "nieve", "marea", "sueño", "calor", "lento", 
    "canto", "roble", "nacer", "pisar", "tigre", 
    "salir", "rueda", "banco", "bicho", "lagos"
]

pool3 = [
    "alado", "albas", "altar", "atizo", "avala",
    "abaco", "abate", "abeja", "aboya", "abran", 
    "cielo", "piano", "sabor", "salud", "pasar",
    "metro", "casas", "flora", "cisne", "citas", 
    "clara", "abeto", "aguas", "agudo", "luces",
    "actor", "busca", "curar", "dagas", "error", 
    "finca", "ganas", "hacer", "islas", "jefas", 
    "moler", "nadar", "obras", "pedir", "quedo", 
    "redes", "sonar", "tabla", "verde", "yogur"
]

# Niveles de dificultad
DIFFICULTY_LEVELS = {
    'soft': (palabras, 6),
    'normal': (pool2, 6),
    'hard': (pool3, 6)
}

# Variables globales
tries = 0 # Intentos comnienza sin ninguno
secrets = "" 
game_running = False # No comienza corriendo el código
current_row = 0  # Para saber en qué fila estamos
entries = []  # Lista para almacenar los cuadros de entrada
label_resultado = None  # Para mostrar el resultado

# Crear ventana principal
root = tk.Tk()
root.title("Wordle Reboot Academy")
root.config(bg="#4d9078")
root.geometry("600x600")  # Establecer un tamaño predeterminado
root.resizable(False, False)  # No se puede redimensionar

# Colores personalizados
COLOR_VERDE = "#90be6d"   # Verde para letras correctas
COLOR_AMARILLO = "#f9c74f"  # Amarillo para letras en posiciones incorrectas
COLOR_GRIS = "#bfbdc1"    # Gris para letras incorrectas

def mostrar_menu():
    """Muestra el menú de selección de dificultad."""
    for widget in root.winfo_children():  # Elimina todo lo anterior en la ventana
        widget.destroy()

    # Crear el menú de selección de dificultad
    label_bienvenida = tk.Label(root,
                                text="¡Bienvenido a Wordle!",
                                bg="#4d9078",
                                fg="white",
                                font=("Courier New", 24, "bold"))
    label_bienvenida.pack(pady=50)

    label_instrucciones = tk.Label(root,
                                   text="Elige un nivel para comenzar:",
                                   bg="#4d9078",
                                   fg="white",
                                   font=("Helvetica", 14, "bold"))
    label_instrucciones.pack(pady=20)

    boton_facil = tk.Button(root,
                            text="Fácil",
                            font=("Helvetica", 12, "bold"),
                            bg="#4d9078",
                            fg="white",
                            borderwidth=5,
                            relief="flat",
                            width=10,
                            height=2,
                            command=lambda: iniciar_juego('soft'))
    boton_facil.pack(pady=5)

    boton_normal = tk.Button(root,
                             text="Normal",
                             font=("Helvetica", 12, "bold"),
                             bg="#4d9078",
                             fg="white",
                             borderwidth=5,
                             relief="flat",
                             width=10,
                             height=2,
                             command=lambda: iniciar_juego('normal'))
    boton_normal.pack(pady=5)

    boton_dificil = tk.Button(root,
                              text="Difícil",
                              font=("Helvetica", 12, "bold"),
                              bg="#4d9078",
                              fg="white",
                              borderwidth=5,
                              relief="flat",
                              width=10,
                              height=2,
                              command=lambda: iniciar_juego('hard'))
    boton_dificil.pack(pady=5)

def iniciar_juego(nivel):
    global tries, secrets, game_running, current_row, entries
    game_running = True
    current_row = 0
    entries = []  # Reiniciar las entradas
    secrets, tries = DIFFICULTY_LEVELS[nivel]
    secrets = random.choice(secrets)  # Elegir palabra secreta
    print(f"Palabra secreta (DEBUG): {secrets}")  # DEBUG
    crear_tablero()  # Crear el tablero para el juego

def crear_tablero():
    """Configura el tablero de juego con las casillas y entradas."""
    for widget in root.winfo_children():  # Elimina todo lo anterior en la ventana
        widget.destroy()

    label_instrucciones = tk.Label(root,
                                   text="Adivina la palabra 'Secreta'",
                                   bg="#4d9078",
                                   fg="white",
                                   font=("Helvetica", 14, "bold"))
    label_instrucciones.pack(pady=20)

    # Crear los cuadros de letras para cada intento
    for i in range(tries):
        fila_frame = tk.Frame(root,
                              bg="#4d9078")  # Un Frame por cada fila de intento
        fila_frame.pack(pady=5)

        fila_entries = []
        for j in range(5):  # Cada palabra tiene 5 letras
            entrada = tk.Entry(fila_frame,
                               width=3,
                               font=("Helvetica", 24),
                               justify='center',
                               state='disabled')
            entrada.grid(row=i, column=j, padx=5)
           
            
            fila_entries.append(entrada)

        entries.append(fila_entries)  # Añadimos la fila de entradas a la lista global

    # Habilitar la primera fila
    habilitar_fila(0)

    # Botón de Comprobar
    global boton_comprobar
    boton_comprobar = tk.Button(root,
                                text="Comprobar",
                                font=("Helvetica", 12, "bold"),
                                bg="white",
                                fg="#4d9078",
                                borderwidth=5,
                                relief="flat",
                                width=10,
                                height=2,
                                command=verificar_palabra)
    boton_comprobar.pack(pady=20)

def habilitar_fila(fila):
    """Habilita las entradas de la fila para que se puedan editar."""
    for entry in entries[fila]:
        entry.config(state="normal")
        entry.bind("<KeyRelease>",
                   lambda e,
                   row=fila,
                   idx=entries[fila].index(entry): mover_foco(e, row, idx))

def mover_foco(event, row, idx):
    """Mueve el foco automáticamente a la siguiente letra en la fila y separa las letras en celdas."""
    # Movimiento con flechas izquierda y derecha
    if event.keysym == 'Left':
        if idx > 0:
            entries[row][idx - 1].focus()
    elif event.keysym == 'Right':
        if idx < 4:
            entries[row][idx + 1].focus()
    
    # Solo permitir un carácter en la celda
    if event.keysym.isalpha() and len(event.char) == 1:
        if len(entries[row][idx].get()) == 0:  # Solo insertar si está vacío
            entries[row][idx].insert(0, event.char)
        return "break"  # Evitar que se inserten más caracteres
    
    # Si el usuario intenta pegar o escribir algo, lo borramos
    if len(entries[row][idx].get()) > 1 or not event.char.isalpha():
        entries[row][idx].delete(1, tk.END)  # Mantener solo el primer carácter



def verificar_palabra():
    """Verifica la palabra ingresada y aplica colores según la coincidencia."""
    global current_row
    if current_row >= tries:
        return  # Si ya se alcanzó el máximo de intentos, no hacer nada más

    # Recoger la palabra ingresada por el usuario
    palabra_usuario = ''.join([entry.get().lower() for entry in entries[current_row]])

    if len(palabra_usuario) != 5:
        return  # Si la palabra no tiene 5 letras, no hacer nada

    # Evaluar la palabra ingresada
    for i, letra in enumerate(palabra_usuario):
        if letra == secrets[i]:  # Letra correcta en la posición correcta
            entries[current_row][i].config(bg=COLOR_VERDE)
        elif letra in secrets:  # Letra en la palabra pero en la posición incorrecta
            entries[current_row][i].config(bg=COLOR_AMARILLO)
        else:  # Letra no está en la palabra
            entries[current_row][i].config(bg=COLOR_GRIS)

    if palabra_usuario == secrets:
        mostrar_resultado(True)
    elif current_row + 1 == tries:
        mostrar_resultado(False)
    else:
        current_row += 1  # Pasar a la siguiente fila
        habilitar_fila(current_row)

def mostrar_resultado(ganador):
    """Muestra si el jugador ha ganado o perdido."""
    global label_resultado
    resultado = "🤩¡Felicidades, has ganado!🤩" if ganador else f"🫣Lo siento, la palabra era '{secrets}'🫣"
    
    if label_resultado:
        label_resultado.destroy()  # Limpiar el resultado anterior

    label_resultado = tk.Label(root,
                               text=resultado,
                               font=("Helvetica", 16, "bold"),
                               bg="#4d9078",
                               fg="white",
                               height=1
                               )
    
    label_resultado.pack(pady=20)

    # Botón para reiniciar juego
    boton_reiniciar = tk.Button(root,
                                text="Reiniciar Juego",
                                font=("Helvetica", 12, "bold"),
                                bg="white",
                                fg="#4d9078",
                                borderwidth=5,
                                relief="flat",
                                width=20,
                                height=5,
                                justify="center",
                                command=mostrar_menu)
    boton_reiniciar.pack(pady=15)

# Iniciar con el menú
mostrar_menu()

# Correr la ventana principal
root.mainloop()
