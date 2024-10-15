import random

palabras = ["actor", "busca", "curar", "dagas", "error", "finca", "ganas", "hacer", "islas", "jefas", "moler", "nadar", "obras", "pedir", "quedo", "redes", "sonar" , "tabla" , "verde",  "yogur" , "zorro"]
secrets = random.choice(palabras)
 
def verificar_palabra(word, secrets):
    word = word.lower()
    secrets = secrets.lower()
 
    if word == secrets:
        return True
    else:
        #letras_correctas = sum(1 for x, y in zip(word, secrets) if x == y)
         
        list_letra = []
        list_emoji = []
        for x, y in zip(secrets, word):
                    if y in secrets and y in x:
                        nice = "  " + y + " "
                        niceE = " 👌"
                        list_letra.append(nice)
                        list_emoji.append(niceE)

                    elif y in secrets:
                        meh = " " + y + " "
                        mehE = " 🙄"
                        list_letra.append(meh)
                        list_emoji.append(mehE)
                    else:
                        bad = " " + y + " "
                        badE = " 👎""medio", "melon", "meter", "metro",
                        list_letra.append(bad)
                        list_emoji.append(badE)

        resultado1 = ' '.join(list_letra)
        resultado2 = ' '.join(list_emoji)

        print(resultado1)
        print(resultado2)
        return False
 
def jugar_wordle():
    intentos = 0
    max_intentos = 6
    while intentos < max_intentos:
        word = input("Ingresa una palabra de 5 letras: ")
 
        if len(word) != 5 or not word.isalpha():
            print("😬 La palabra debe tener 5 letras y no contener números ni carácteres especiales. Inténtalo de nuevo. 😬\n")
            continue
            
 
        if verificar_palabra(word, secrets):
            print("\n🤩 ¡Felicidades! Has adivinado la palabra. 🤩")
            break
 
        intentos += 1
        print(f"Intento {intentos}/{max_intentos}\n")
 
    if intentos == max_intentos:
        print(f"😞 Lo siento, has alcanzado el máximo de intentos. La palabra secreta era '{secrets}'. 🫣")
 
jugar_wordle()
