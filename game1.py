import random
import emoji

def game1():
    objects = ["papel", "tijeras", "piedra"]
    count = 0
    victorias = 0
    derrotas = 0
    empates = 0
    print("***********************************************")
    print("* Bienvenido jugador, ¡preparate! ＼(＾▽＾)／ *")
    print("***********************************************")

    while count <= 2 :
        print(count)
        print(emoji.emojize("\n:firecracker: Elige tu arma :firecracker: ┗(•̀へ •́ ╮ )"))
        user = input(emoji.emojize("\npiedra \U0001F44A, papel \U0001F590 o tijeras: "))
        program = random.choice(objects)

        if user == "papel" or user == "piedra" or user == "tijeras":
            print(f"Has elegido {user}.")
        else:
            print(emoji.emojize("Vuelve a elegir. \U0001F624"))
            continue
        
        count += 1 
        print(f"Llevas {count} intento(s)")

        if user == program:
            print("Empate")
            empates += 1
        elif user == "papel":
            if program == "tijeras":
                print("Perdiste")
                derrotas += 1
            else:
                print("Ganaste")
                victorias += 1
        elif user == "piedra":
            if program == "tijeras":
                print("Ganaste")
                victorias += 1
            else:
                print("Perdiste")
                derrotas += 1
        elif user == "tijeras":
            if program == "piedra":
                print("Perdiste")
                derrotas += 1
            else:
                print("Ganaste")
                victorias += 1
            continue

    if victorias >= 2:
        print("\nEnorabuena, ganaste a la máquina, ¡¡¡¡MÀQUINAAAAAAAAAA!!!!(┛｀Д´)┛彡┻━┻ ")
    elif derrotas >= 2:
        print("\nTe ganó una máquina, haztelo mirar. (✧≖‿ゝ≖)")
    elif empates >= 2:
        print("\nEmpante (⊙_☉), try again.")
    else:
        print("\nNo bebé, otro día será. ღ(U ω Uღ)")

game1()
print("\nHas acabado este juego. 凸(｡◕‿◕｡)凸")   