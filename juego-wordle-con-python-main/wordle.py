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

# Definición de constantes
DIFFICULTY_LEVELS = {
    'soft': (palabras, 6),
    'normal': (pool2, 5),
    'hard': (pool3, 4)
}

# Inicialización de variables
tries = 0
secrets = ""

# Colores usando secuencias ANSI
COLOR_VERDE = "\033[92m"
COLOR_AMARILLO = "\033[93m"
COLOR_GRIS = "\033[90m"
COLOR_RESET = "\033[0m"

def elegir_dificultad():
    """Permite al usuario elegir la dificultad del juego."""
    global tries, secrets
    print("Dificultades disponibles: soft, normal, hard")
    user_difficulty = input("Elige la dificultad de juego: ").lower()
    
    if user_difficulty in DIFFICULTY_LEVELS:
        secrets, tries = DIFFICULTY_LEVELS[user_difficulty]
        secrets = random.choice(secrets)  # Elegir una palabra secreta
    else:
        print("\nPor favor elige una dificultad válida.")
        elegir_dificultad()

def verificar_palabra(word, secrets):
    """Verifica la palabra ingresada y proporciona retroalimentación."""
    word = word.lower()
    feedback = []
    
    for i, letter in enumerate(word):
        if letter == secrets[i]:
            feedback.append(f"{COLOR_VERDE}{letter}{COLOR_RESET}")  # Letra correcta en la posición correcta (verde)
        elif letter in secrets:
            feedback.append(f"{COLOR_AMARILLO}{letter}{COLOR_RESET}")  # Letra correcta en posición incorrecta (amarillo)
        else:
            feedback.append(f"{COLOR_GRIS}{letter}{COLOR_RESET}")  # Letra incorrecta (gris)
    
    resultado = ' '.join(feedback)
    print(f"\nRetroalimentación: {resultado}")
    
    return word == secrets  # Devuelve True si la palabra es correcta

def jugar_wordle():
    """Lógica principal del juego."""
    intentos = 0
    max_intentos = tries
    
    while intentos < max_intentos:
        word = input("\nIngresa una palabra de 5 letras, no hay acentos 😉: ")
        
        if len(word) != 5 or not word.isalpha():
            print("😬 La palabra debe tener 5 letras y no contener números ni carácteres especiales. Inténtalo de nuevo. 😬\n")
            continue

        if verificar_palabra(word, secrets):
            print("\n🤩 ¡Felicidades! Has adivinado la palabra. 🤩")
            break

        intentos += 1
        print(f"\nIntento {intentos}/{max_intentos}\n")
    
    if intentos == max_intentos:
        print(f"😞 Lo siento, has alcanzado el máximo de intentos. La palabra secreta era '{secrets}'. 🫣")

# Ejecución del juego
elegir_dificultad()
jugar_wordle()
