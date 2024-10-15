from tkinter import  Tk, Button, Entry, Label, messagebox, PhotoImage
from tkinter import  StringVar,Frame
import random

palabras = ["actor", "busca", "curar", "dagas", "error", "finca", "ganas", "hacer", "islas", "jefas", "moler", "nadar", "obras", "pedir", "quedo", "redes", "sonar" , "tabla" , "verde",  "yogur" , "zorro"]
pool2 = ["perro", "gatos", "medio", "melon", "meter", "metro", "casas", "flora", "cisne", "citas", "clara", "abeto", "aguas", "agudo", "luces", "mujer", "coche", "silla", "mesas", "jugar", "cielo", "piano", "sabor", "salud", "pasar", "nieve", "marea", "sueño", "calor", "lento", "canto", "roble", "nacer", "pisar", "tigre", "salir", "rueda", "banco", "bicho", "lagos"]
pool3 = [
"alado", "albas", "altar", "atizo", "avala", "lente", "mujer", "nacer", 
"abaco", "abate", "abeja", "aboya", "abran", "abras", "acoja", "acojo",
"acres", "actas", "actos", "actuo", "acuna", "acune", "acuso", "acusó",
"afeas", "aguda", "alaju", "alces", "aldea", "aleja", "algas", "alias",
"altos", "amina", "andas", "andes", "anear", "anima", "anima", "atojo",
"azote", "aerea", "anoro", "bache", "babas", "bacas", "bajes", "bebes",
"belen", "berto", "bicho", "bizco", "busca", "bajos", "barre", "batas",
"bates", "bayas", "bebed", "besen", "besos", "bojar", "bonos", "borre",
"borra", "botad", "botes", "bruno", "bruta", "bruto", "cabra", "cafes",
"cajas", "calar", "calas", "calca", "calco", "calla", "calma", "camba",
"canto", "capto", "caras", "carga", "cargo", "carlo", "carro", "casas",
"catar", "caida", "cejas", "celia", "cenas", "cepas", "cerca", "cerco",
"cerdo", "cerda", "chile", "ciego", "ciega", "claro", "clave", "clavo", 
"colas", "colon", "colon", "coral", "coras", "corea", "corro", "costo", 
"coste", "crudo", "curdo", "curda", "curar", "celta", "combo", "corse", 
"crema", "cuida", "culos", "cural", "dados", "dagas", "danos", "danza", 
"dejar", "dejes", "denso", "densa", "dices", "kiwis", "xenon", "valer",
"divos", "dotes", "dunas", "dures", "duros", "dubai", "enojo", "echas",
"edito", "edita", "elevo", "emule", "enoje", "error", "errar", "elena",
"emoji", "envio", "erizo", "espia", "euros", "fallo", "falto", "feria",
"fetos", "fijos", "filas", "filia", "finca", "fetos", "firma", "floto",
"focos", "folla", "forma", "frida", "frita", "fugaz", "gales", "gafas",
"galas", "galia", "galos", "ganas", "gases", "gasto", "girar", "gerbo",
"gordo", "gorda", "gorro", "grave", "grava", "grito", "gabon", "ghana",
"gemir", "guera", "guero", "hacer", "halos", "hasta", "harta", "hielo",
"habas", "habla", "hacha", "haiti", "hijas", "hijos", "huera", "huero",
"india", "indio", "ideas", "inflo", "islas", "ivana", "jefas", "jefes",
"jerga", "josue", "juego", "jugar", "jadeo", "jairo", "jalon", "jesus",
"joder", "jurar", "kabul", "kenia", "kurdo", "kurda", "labia", "lacra",
"lados", "lagos", "lance", "larga", "largo", "lejos", "lenta", "lento",
"libia", "libro", "libra", "linda", "lindo", "logro", "loteo", "luche",
"mania", "malos", "malas", "marca", "marco", "marti", "marte", "marta",
"marta", "maria", "mario", "molar", "moler", "monte", "manco", "manca", 
"macao", "malta", "mango", "manga", "meaba", "media", "midas", "midas",
"minsk", "mirar", "miron", "mojar", "multa", "mundo", "nacer", "nadar", 
"narro", "natas", "naves", "necio", "necia", "ninos", "notas", "nubes", 
"nuria", "nabos", "nazis", "nepal", "niger", "noñez", "nizca", "nuzco", 
"noqui", "nurdo", "nurda", "opera", "obras", "ocios", "ollas", "ondas", 
"onzas", "ovulo", "oreja", "odiár", "orina", "ortos", "osito", "palas", 
"pedir", "pelea", "pelar", "peras", "azote", "manco", "yacer", "zapas",
"perro", "perra", "pilas", "pinto", "poder", "pacto", "pagar", "palma",
"papua", "parda", "pardo", "paseo", "pecio", "penes", "peres", "pesca",
"pifia", "pisco", "playa", "pleno", "punto", "purga", "queda", "quedo",
"quede", "quema", "queso", "quepa", "reloj", "rubio", "rubia", "rasco",
"rasca", "ratas", "rasta", "redes", "remar", "renos", "renta", "rabia",
"rabos", "rabal", "ramos", "ramon", "raspa", "recio", "recia", "regio",
"resto", "rugir", "rogar", "sabio", "sabia", "savia", "sacar", "salar",
"salir", "selva", "sanar", "sopas", "secar", "serio", "seria", "situo",
"sobar", "sonar", "subir", "sucio", "sucia", "sacra", "sajon", "salve",
"salva", "salto", "salud", "samoa", "santo", "santa", "sedar", "sexos",
"segar", "siega", "siria", "sobar", "sobre", "solar", "sonda", "soplo",
"sonar", "sudan", "sueno", "suiza", "sushi", "super", "tabla", "tacos",
"tania", "tapas", "tapar", "tazas", "telon", "tener", "tejer", "tenis",
"terco", "terca", "terso", "tersa", "tipos", "tirar", "todas", "todos",
"tomar", "tonos", "tonto", "tonta", "toque", "torpe", "trote", "talar",
"telar", "tarde", "temer", "tenia", "topar", "tocar", "toser", "toner",
"traer", "tumba", "tunez", "unoso", "unosa", "untes", "urbes", "urnas",
"valer", "vacas", "vagos", "vagas", "valor", "veces", "vedas", "velas",
"velar", "vemos", "verse", "verso", "venir", "verde", "vigor", "vivir",
"volar", "votar", "vasco", "vasca", "vasto", "vasta", "viaje", "video",
"weber", "wikis", "wones", "xolas", "yemen", "yates", "yemas", "yendo",
"yenes", "sabor", "tigre", "zurdo", "orcas", "pinta", "quien", "risas",
"abaco", "eflux", "yabal", "kefir", "laxar", "islas", "jugar", "karma", 
"aboya", "amina", "hotel", "juego", "kilos", "fuego", "gente", "huevo", 
"lucir", "mango", "nieve", "oliva", "piano", "coche", "dolar", "elijo",
"quema", "rango", "sello", "tigre", "dedos", "zorro", "viejo", "broma"
]    
class Game(Frame):
     def __init__(self, master):
          super().__init__( master)
          self.fila = 0
          self.verde = '#C5EBC3'
          self.naranjado = '#D6AC57'
          self.gris = '#B6B6B5'
          self.texto = StringVar()
          self.texto.trace_add("w", lambda *args: self.limitar(self.texto))
          self.create_widgets()
          self.dificultad()


     def dificultad(self):
          # Eliminar cualquier widget existente antes de crear los botones de dificultad
          for widget in self.winfo_children():
               widget.destroy()
          # Crear el Label de bienvenida
          Label(
               self,
               text="Bienvenidos a WORDLE - Elige la dificultad",
               fg="white",
               bg="black",
               justify="center",
               font=("Courier", 16)
          ).pack(pady=20)

          # Botón para 'Soft'
          Button(
               self,
               text="Soft",
               font=("Courier", 14),
               bg="#B7C8B5",
               fg="white",
               command=lambda: self.iniciar_juego("soft")
          ).pack(pady=10)

          # Botón para 'Normal'
          Button(
               self,
               text="Normal",
               font=("Courier", 14),
               bg="#B7C8B5",
               fg="white",
               command=lambda: self.iniciar_juego("normal")
          ).pack(pady=10)

          # Botón para 'Hard'
          Button(
               self,
               text="Hard",
               font=("Courier", 14),
               bg="#B7C8B5",
               fg="white",
               command=lambda: self.iniciar_juego("hard")
          ).pack(pady=10)


     def iniciar_juego(self, dificultad):
          global tries
          if dificultad== 'soft':
               self.secrets = random.choice(palabras)
               self.tries = 6
          elif dificultad== 'normal':
               self.secrets = random.choice(pool2)
               self.tries -= 1
          elif dificultad== 'hard':
               self.secrets = random.choice(pool3)
               self.tries -= 2
          
     

     def verificar_palabra(word, secrets):
          word = word.lower()
          secrets = secrets.lower()
          if word == secrets:
               return True
          else:
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
     
     def limitar(self, texto):
	     if len(texto.get()) > 5:
	          texto.set(texto.get()[:5])


root = Tk()
#Dimensiones
root.geometry('600x500+500+50')
#color fondo
root.configure(background="#353839")
#Titulo ventana
Tk.title(root, "WORDLE GAMES!")

Label(
     root,
     text="Bienvenidos a WORDLE",
     fg="white",
     bg="black",
     justify="center"
).pack()

 #Boton
Button(
     root,
     text="Soft",
     font=("Courier",14),
     bg="#B7C8B5",
     fg="white",
     command=Game.dificultad
).pack()

# #Boton
Button(
     root,
     text="Normal",
     font=("Courier",14),
     bg="#B7C8B5",
     fg="white",
     command=Game.dificultad
).pack()

# #Boton
Button(
     root,
     text="Hard",
     font=("Courier",14),
     bg="#B7C8B5",
     fg="white",
     command=Game.dificultad         
).pack()

root.mainloop()