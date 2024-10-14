import random
 
palabras = ["actor", "busca", "curar", "dagas", "error", "finca", "ganas", "hacer", "islas", "jefas", "moler", "nadar", "obras", "pedir", "quedo", "redes", "sonar" , "tabla" , "verde",  "yogur" , "zorro"]
secrets = random.choice(palabras)
 
def verificar_palabra(word, secrets):
    word = word.lower()
    secrets = secrets.lower()
 
    if word == secrets:
        return True
    else:
        letras_correctas = sum(1 for x, y in zip(word, secrets) if x == y)
        print(f"Letras correctas: {letras_correctas}")

        for i in secrets:
            for e in word:
                




        return False
 
def jugar_wordle():
    intentos = 0
    max_intentos = 6
 
    while intentos < max_intentos:
        word = input("Ingresa una palabra de 5 letras: ")
 
        if len(word) != 5:
            print("La palabra debe tener 5 letras. Inténtalo de nuevo.")
            continue
 
        if verificar_palabra(word, secrets):
            print("¡Felicidades! Has adivinado la palabra.")
            break
 
        intentos += 1
        print(f"Intento {intentos}/{max_intentos}")
 
    if intentos == max_intentos:
        print(f"Lo siento, has alcanzado el máximo de intentos. La palabra secreta era '{secrets}'.")
 
jugar_wordle()
