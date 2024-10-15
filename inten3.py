import random
# import tkinter

palabras = ["actor", "busca", "curar", "dagas", "error", "finca", "ganas", "hacer", "islas", "jefas", "moler", "nadar", "obras", "pedir", "quedo", "redes", "sonar" , "tabla" , "verde",  "yogur" , "zorro"]
pool2 = ["perro", "gatos", "casas", "flora", "luces", "mujer", "coche", "silla", "mesas", "jugar", "cielo", "piano", "sabor", "salud", "pasar", "nieve", "marea", "sueño", "calor", "lento", "canto", "roble", "nacer", "pisar", "tigre", "salir", "rueda", "banco", "bicho", "lagos"]
pool3 = [
    "abeto", "aguas", "agudo", "alado", "albas", "altar", "atizo", "avala",
    "abaco", "abate", "abeja", "aboya", "abran", "abras", "acoja", "acojo",
    "acres", "actas", "actos", "actúo", "acuna", "acune", "acuso", "acusó",
    "afeas", "aguda", "alajú", "alces", "aldea", "aleja", "algas", "alias",
    "altos", "amina", "andas", "andes", "anear", "anima", "ánima", "atojo",
    "azote", "aérea", "añoro", "bache", "babas", "bacas", "bajes", "bebés",
    "belén", "berto", "bicho", "bizco", "busca", "bajos", "barre", "batas",
    "bates", "bayas", "bebed", "bebes", "besen", "besos", "bojar", "bonos",
    "borre", "borra", "botad", "botes", "bruno", "bruta", "bruto", "cabra",
    "cafés", "cajas", "calar", "calas", "calca", "calco", "calla", "calma",
    "camba", "canto", "capto", "caras", "carga", "cargo", "carlo", "carro",
    "casas", "catar", "caída", "cejas", "celia", "cenas", "cepas", "cerca",
    "cerco", "cerdo", "cerda", "chile", "ciego", "ciega", "cisne", "citas",
    "clara", "claro", "clave", "clavo", "colas", "colon", "colón", "coral",
    "coras", "corea", "corro", "costo", "coste", "crudo", "curdo", "curda",
    "curar", "celta", "combo", "corsé", "crema", "cuida", "culos", "cural",
    "dados", "dagas", "daños", "danza", "dejar", "dejes", "denso", "densa",
    "dices", "divos", "dotes", "dunas", "dures", "duros", "dubái", "enojo",
    "echas", "edito", "edita", "elevo", "emulé", "enoje", "error", "errar",
    "elena", "emoji", "envío", "erizo", "espía", "euros", "fallo", "falto",
    "feria", "fetos", "fijos", "filas", "filia", "finca", "fetos", "firma",
    "floto", "focos", "folla", "forma", "frida", "frita", "fugaz", "gales",
    "gafas", "galas", "galia", "galos", "ganas", "gases", "gasto", "girar",
    "gerbo", "gordo", "gorda", "gorro", "grave", "grava", "grito", "gabón",
    "ghana", "gemir", "güera", "güero", "hacer", "halos", "hasta", "harta",
    "hielo", "habas", "habla", "hacha", "haití", "hijas", "hijos", "huera",
    "huero", "india", "indio", "ideas", "inflo", "islas", "ivana", "jefas",
    "jefes", "jerga", "josué", "juego", "jugar", "jadeo", "jairo", "jalón",
    "jesús", "joder", "jurar", "kabul", "kenia", "kurdo", "kurda", "labia",
    "lacra", "lados", "lagos", "lance", "larga", "largo", "lejos", "lenta",
    "lento", "libia", "libro", "libra", "linda", "lindo", "logro", "loteo",
    "luche", "manía", "malos", "malas", "marca", "marco", "martí", "marte",
    "marta", "marta", "maría", "mario", "medio", "melón", "meter", "metro",
    "molar", "moler", "monte", "manco", "manca", "macao", "malta", "mango",
    "manga", "meaba", "media", "midas", "midas", "minsk", "mirar", "mirón",
    "mojar", "multa", "mundo", "nacer", "nadar", "narro", "natas", "naves",
    "necio", "necia", "niños", "notas", "nubes", "nuria", "nabos", "nazis",
    "nepal", "níger", "ñoñez", "ñizca", "ñuzco", "ñoqui", "ñurdo", "ñurda",
    "ópera", "obras", "ocios", "ollas", "ondas", "onzas", "óvulo", "oreja",
    "odiár", "orina", "ortos", "osito", "palas", "pedir", "pelea", "pelar",
    "peras", "perro", "perra", "pilas", "pinto", "poder", "pacto", "pagar",
    "palma", "papúa", "parda", "pardo", "paseo", "pecio", "penes", "peres",
    "pesca", "pifia", "pisco", "playa", "pleno", "punto", "purga", "queda",
    "quedo", "quede", "quema", "queso", "quepa", "reloj", "rubio", "rubia",
    "rasco", "rasca", "ratas", "rasta", "redes", "remar", "renos", "renta",
    "rabia", "rabos", "rabal", "ramos", "ramón", "raspa", "recio", "recia",
    "regio", "resto", "rugir", "rogar", "sabio", "sabia", "savia", "sacar",
    "salar", "salir", "selva", "sanar", "sopas", "secar", "serio", "seria",
    "sitúo", "sobar", "sonar", "subir", "sucio", "sucia", "sacra", "sajón",
    "salve", "salva", "salto", "salud", "samoa", "santo", "santa", "sedar",
    "sexos", "segar", "siega", "siria", "sobar", "sobre", "solar", "sonda",
    "soplo", "soñar", "sudán", "sueño", "suiza", "sushi", "súper", "tabla",
    "tacos", "tania", "tapas", "tapár", "tazas", "telón", "tener", "tejer",
    "tenis", "terco", "terca", "terso", "tersa", "tipos", "tirar", "todas",
    "todos", "tomar", "tonos", "tonto", "tonta", "toque", "torpe", "trote",
    "talar", "telar", "tarde", "temer", "tenia", "topar", "tocar", "toser",
    "tóner", "traer", "tumba", "túnez", "uñoso", "uñosa", "untes", "urbes",
    "urnas", "valer", "vacas", "vagos", "vagas", "valor", "veces", "vedas",
    "velas", "velar", "vemos", "verse", "verso", "venir", "verde", "vigor",
    "vivir", "volar", "votar", "vasco", "vasca", "vasto", "vasta", "viajes",
    "vídeo", "weber", "wikis", "wones", "xolas", "yemen", "yates", "yemas",
    "yendo", "yenes",
    "abaco", "eflux", "yabal", "kefir", "laxar", 
    "aboya", "amina", "hotel", "juego", "kilos", 
    "lucir", "mango", "nieve", "oliva", "piano", 
    "quema", "rango", "sello", "tigre", "dedos", 
    "juego", "zorro", "viejo", "broma", "coche", 
    "dolar", "elijo", "fuego", "gente", "huevo", 
    "islas", "jugar", "karma", "lente", "mujer", 
    "nacer", "orcas", "pinta", "quien", "risas", 
    "sabor", "tigre", "zurdo", "valer", "kiwis", 
    "xenon", "yacer", "zapas", "azote", "manco"
]

#secrets = random.choice(palabras)

def dificultad():

    print("soft, normal, hard") 
    user_dif = input("Elige la dificultad de juego: ").lower()
    global tries
    tries = 6

    
    if user_dif == 'soft':
         secrets = random.choice(palabras)
         tries = 6
    elif user_dif == 'normal':
         secrets = random.choice(pool2)
         tries -= 1
    elif user_dif == 'hard':
         secrets = random.choice(pool3)
         tries -= 2
    else:
         print("\nPor favor elige una dificultad.")
         dificultad()
        
 
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
                            badE = " 👎"
                            list_letra.append(bad)
                            list_emoji.append(badE)

            resultado1 = ' '.join(list_letra)
            resultado2 = ' '.join(list_emoji)

            print(f"\n{resultado1}")
            print(resultado2)
            return False
    
    def jugar_wordle():
    
        intentos = 0
        max_intentos = tries
        while intentos < max_intentos:
            word = input("\nIngresa una palabra de 5 letras: ")
    
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
    jugar_wordle()

dificultad()
