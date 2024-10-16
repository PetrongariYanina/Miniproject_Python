import random
import emoji

def game1():
    objects = ["papel", "tijeras", "piedra"]
    count = 0
    victorias = 0
    derrotas = 0
    empates = 0
    
    print("***********************************************")
    print("* Bienvenido jugador, ¡prepárate! ＼(＾▽＾)／ *")
    print("***********************************************")

    while count < 3:  # Cambié <= 2 por < 3 para que sean exactamente 3 intentos.
        print(f"\nIntento {count + 1}:")  # Mostrar el intento actual.
        user = input(emoji.emojize("\nElige tu arma: piedra \U0001F44A, papel \U0001F590 o tijeras: ")).lower()  # Uso de .lower() para hacer la entrada insensible a mayúsculas.

        if user not in objects:  # Verifica si la opción del usuario es válida.
            print(emoji.emojize("Opción no válida. Vuelve a elegir. \U0001F624"))
            continue
        
        program = random.choice(objects)  # Elección aleatoria de la máquina.
        print(f"Has elegido {user}. La máquina eligió {program}.")

        if user == program:
            print("Empate")
            empates += 1
        elif (user == "papel" and program == "piedra") or \
             (user == "piedra" and program == "tijeras") or \
             (user == "tijeras" and program == "papel"):
            print("Ganaste")
            victorias += 1
        else:
            print("Perdiste")
            derrotas += 1
        
        count += 1  # Contar intentos aquí, después de procesar la elección.

    # Mensajes finales según el resultado
    if victorias > derrotas and victorias > empates:
        print("\n¡Enhorabuena, ganaste a la máquina, ¡¡¡¡MÀQUINAAAAAAAAAA!!!!(┛｀Д´)┛彡┻━┻ ")
    elif derrotas > victorias and derrotas > empates:
        print("\nTe ganó una máquina, ¡haztelo mirar! (✧≖‿≖)")
    elif empates > victorias and empates > derrotas:
        print("\nEmpate total (⊙_☉), intenta de nuevo.")
    else:
        print("\nNo bebé, otro día será. ღ(U ω Uღ)")

game1()
print("\nHas acabado este juego. 凸(｡◕‿◕｡)凸")
