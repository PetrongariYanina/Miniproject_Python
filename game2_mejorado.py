import os
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_color(simons_colors, colors):
    """Añade un color aleatorio a la secuencia de Simón."""
    simons_colors.append(random.choice(colors))

def user_turn():
    """Obtiene la entrada del usuario y la convierte a mayúsculas."""
    turn = input("Tu turno:\n").upper()
    return turn

def main():
    colors = ["R", "G", "B", "Y"]
    simons_colors = []
    clear()
    time.sleep(1)

    # Aquí puedes decidir cuántos colores iniciales quieres agregar, por ahora comienza con 0
    for _ in range(0):  # Puedes cambiar este rango para empezar con más colores.
        add_color(simons_colors, colors)

    print('''
          11111111111111111111111111111
    11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    1111111111¶¶¶¶¶111_________________¶¶
    11111111¶¶1_______1111______111_____¶¶
    111111¶¶______11_________11111111____¶1
    111111¶____11___1_____11______1111___1¶
    11111¶1___1_____1_____1_________1_____¶1
    11111¶__________________1¶¶¶¶1________1¶
    1111¶¶_____¶¶¶¶1______1¶¶_¶¶¶¶¶1_______¶¶
    111¶¶_1_1_¶¶¶¶¶¶¶_1___¶__1¶¶¶¶¶¶111____1¶¶
    111¶_1________11¶¶1___¶¶¶1__1_____1¶¶¶1__1¶
    11¶1__1¶¶1______11_____1____¶¶__1¶¶1__¶¶__1¶
    11¶1__111¶¶¶¶___¶1___________1¶¶1___¶__¶1__¶
    11¶1____1_11___¶¶_____1¶1_________¶¶¶1__¶__¶1
    111¶_1__¶____1¶¶______11¶1_____1¶¶1_¶¶¶1¶__¶1
    111¶1__¶¶___11¶¶____¶¶¶_¶___1¶¶¶1___¶__¶___¶1
    111¶¶__¶¶¶1_____¶¶1_____11¶¶¶1_¶__1¶¶_____¶11
    1111¶__¶¶1¶¶¶1___¶___1¶¶¶¶1____¶¶¶¶¶_____¶¶11
    1111¶__¶_1__¶¶¶¶¶¶¶¶¶11__¶__1¶¶¶1_¶_____¶¶111
    1111¶1_¶¶¶__1___¶___1____¶¶¶¶¶1¶_¶¶____¶¶1111
    1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___1¶¶_____¶11111
    1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___¶¶_____¶¶11111
    1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1__¶¶______¶111111
    1111¶__1¶¶_¶_¶__¶___11____1¶¶¶______1¶1111111
    1111¶___¶¶1¶_11_11__1¶__1¶¶¶1___11_1¶11111111
    1111¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111
    1111¶__________11111_______111_1¶¶11111111111
    1111¶_1__11____________1111__1¶¶1111111111111
    1111¶__11__1________1111___1¶¶111111111111111
    1111¶___1111_____________1¶¶11111111111111111
    1111¶¶_______________11¶¶¶1111111111111111111
    11111¶¶__________1¶¶¶¶¶1111111111111111111111
    1111111¶¶¶¶¶¶¶¶¶¶¶111111111111111111111111111
    111111111111111111111111111111111111111111111
          ''')

    print("******************************************")
    print("*  Bienvenido jugador, toma nota (╭ರ_•́)  *")
    print("******************************************")
    time.sleep(3)

    while True:
        add_color(simons_colors, colors)  # Agregar un nuevo color a la secuencia
        sequence = ''.join(simons_colors)  # Crear la secuencia a partir de la lista
        print("Simon dice:")
        time.sleep(1)
        clear()

        for color in simons_colors:  # Mostrar cada color en la secuencia
            print(f"Simon dice: {color}")
            time.sleep(1)
            clear()
        
        if user_turn() == sequence:  # Comprobar si la entrada del usuario es correcta
            clear()
        else:           
            clear()
            print("GAME OVER 〜(꒪꒳꒪)〜")
            break

if __name__ == "__main__":
    main()
