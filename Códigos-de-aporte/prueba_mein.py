import random
import string
import time
from tabulate import tabulate

# Pregunta al jugador como quiere jugar
def configuration_game(configuration:dict) -> dict: 
    # Caracteres
    while True:
        data_value = input("    1- Tipo de caracteres (letras, numeros, ambos): ")
        if data_value in {"letras", "numeros", "ambos"}:
            configuration["Data"] = data_value
            break
        else:
            print("No esta dentro de las opciones (⩺_⩹)")

    # Capitalización
    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        while True:
            capital_value = input("    2- Capitalizacion de letras (mayusculas, minusculas, ambas): ")
            if capital_value in {"mayusculas", "minusculas", "ambas"}:
                configuration["Capital"] = capital_value
                break
            else:
                print("No esta dentro de las opciones (⩺_⩹)")
    else:
        pass
    
    # Repetición
    while True:
        repetition_value = input("    3- Repetición de caracteres (si, no): ")
        if repetition_value == "si" or repetition_value == "no":
            configuration["Repetition"] = repetition_value
            break
        else:
            print("ಠ_ʖಠ ... si o no")
    
    # Cantidad de intentos
    while True:
        amount_value = int(input("    4- Cantidad de caracteres (3-10): "))
        if amount_value >= 3 and amount_value <= 10:
            configuration["Amount"] = amount_value
            break
        else:
            print("Puedes usar 3, 4, 5, 6 ... ಠ_ʖಠ ... 7, 8, 9, 10")

    # Vidas (intentos para adivinar)
    while True:
        lifes_value = input("    5- Intentos (3, 5, 10, infinitos): ")
        if lifes_value == 3 or lifes_value == 5 or lifes_value == 10 or lifes_value == "infinitos":
            """
            if lifes_value == "infinitos": 
                lifes_value = float('inf')
            else: 
                lifes_value = int(lifes_value)
            """
            configuration["Lifes"] = lifes_value
            break
        else:
            print("Opcion NO disponible -(`෴´)- ")

    # Imprimir el diccionario en forma de tabla
    configuration_tab = tabulate(configuration.items(), tablefmt= "grid")

    return configuration_tab

# Genera la cadena por adivinar
def random_combination(configuration:dict) -> list: 
    # Lista para guardar los caracteres con los que se genera la cadena
    options = [] 
    mayus = string.ascii_uppercase # Mayusculas
    minus = string.ascii_lowercase # Minusculas
    mayus_minus = string.ascii_letters # Ambas
    nume = string.digits # Numeros

    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        match configuration["Capital"]:
            case "mayusculas":
                options.append(mayus)
            case "minusculas":
                options.append(minus)
            case "ambas":
                options.append(mayus_minus)

    if configuration["Data"] == "numeros" or configuration["Data"] == "ambos":
        options.append(nume)
    
    options_string = "".join(options)
    lon = configuration["Amount"]

    # Generar cadena aleatoria
    if configuration["Repetition"] == "no":
        chain = "".join(random.sample(options_string, lon))
    else:
        chain = "".join(random.choices(options_string, k = lon))
 
    # Convertir cadena a lista
    chain_list = []
    for elem in chain:
        chain_list.append(elem)

    return chain_list

# Print de carga, for a dramatic flare 
def loading(text: str):
    for i in text: # recorre cada caracter del string
        print(i, end="") # va imprimiendolo uno por uno conforme avanza
        time.sleep(0.2) # retrasa la siguiente accion 2 decimas de segundo

# String a lista (Parar lista-respuesta y lista-usuario) 
def strToList (secuencia : str) -> list:
    return list(secuencia)

# Verifica si la entrada del usuario contiene solo caracteres permitidos
def validate(usuario_input:str, configuration:dict) -> bool:
    allowed_characters = ""
    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        if configuration["Capital"] == "mayusculas":
            allowed_characters += string.ascii_uppercase
        elif configuration["Capital"] == "minusculas":
            allowed_characters += string.ascii_lowercase
        elif configuration["Capital"] == "ambas":
            allowed_characters += string.ascii_letters

    if configuration["Data"] == "numeros" or configuration["Data"] == "ambos":
        allowed_characters += string.digits

    if all(char in allowed_characters for char in usuario_input) == False : 
        validacion : bool = False
        loading (". . .")
        print ("Mmm... \n")
        print ("¿No recuerdas como configuraste la partida?(ﾉಠдಠ)ﾉ︵┻━┻")
    else:
        validacion : bool = True
        loading ("♥°˖✧°˖✧°˖✧°˖✧°˖✧◝(⁰▿⁰)◜✧˖°✧˖°✧˖°✧˖°♥")
    return validacion 

# Leaderboard
def history(user_tries:list, name:str, score:int) -> dict:
    # Crea un diccionario por cada partida jugada, guarda los diccionarios en una lista
    partida = {
        "Nombre" : name,
        "Puntaje" : score
    }
    user_tries.append(partida)
    
    # Ordenar la lista de intentos por puntaje de mayor a menor
    user_tries.sort(key=lambda x: x["Puntaje"], reverse=True)

    for rank, dic in enumerate(user_tries, start= 1):
        dic["rank"] = rank

    # Imprimir el diccionario en forma de tabla
    user_tries_tab = tabulate(user_tries, headers= "keys", tablefmt= "grid")
    return user_tries_tab

# Comparar lista-respuesta con lista-usuario (Revisa que las dos sean iguales de largas)
def compareLengths (listR, listU : list) -> int:
    score : int = 0
    
    if len(listR) == len(listU):
        score = 0
        print("LGFG!!! Son del mismo largo (づ ◕‿◕ )づ")
    elif len(listR) > len(listU):
        score = -1
        print("Tch!!! la secuencia es mas larga de lo que ingresaste")
        time.sleep(2)
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        time.sleep(2)
        loading("(-1) punto, por atembao") 
    else: 
        score = -1
        print("Tch!!! la secuencia es mas corta de lo que ingresaste")
        time.sleep(2)
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        time.sleep(2)
        loading("(-1) punto, por atembao") 
    return score

# Comparar mayusculas minúsculas de las listas
def compareCapnoCap (listR: list, listU : list) -> tuple[int, bool]:
    score : int = 0
    capU : list = []
    noCapU : list = []
    flagT : list = []

    for i in listU:
        if i.isalpha() and i.isupper(): # Verificar si el carácter es alfabético y mayúscula
            capU.append(i)
        elif i.isalpha() and i.islower(): # Verificar si el carácter es alfabético y minúscula
            noCapU.append(i) 

    for i in listR:
        if i in capU and i in noCapU:
            score += 2
            flagT.append(True) 
            time.sleep(2)
            print (f"\nOh! parece que {i} si se encuentra en la lista tanto en mayuscula como minuscula")
            print ("Un piko por inteliegente ( ˘ ³˘)♥")
            print ("(+2) puntos")
        elif i in capU and i not in noCapU:
            score += 1
            flagT.append(False) 
            time.sleep(2)
            print (f"\nOh! parece que {i} si se encuentra en la lista en mayuscula pero no en minuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        elif i not in capU and i in noCapU:
            score += 1
            flagT.append(False) 
            time.sleep(2)
            print (f"\nOh! parece que {i} si se encuentra en la lista en minuscula pero no en mayuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        else:  
            time.sleep(2)
            loading(f"\n{i} Ah dale, obvio, claro, claro (•ิ _•ิ )...")  

    if all(flagT) == True:
        flag = True 
    else:
        flag = False 
    return score, flag  

# Crea una lista con los caracteres que coinciden en posicion
def compare_index(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    flagT : list = []
    both_index = []
    bot = zip(org_chain, user_chain)
    both = list(bot)

    for org, user in both:
        if org == user:
            both_index.append(user)
        else:
            pass

    if len(both_index) == len(org_chain):
        flagT.append(True) 
    else:
        flagT.append(False) 
        match len(both_index):
            case 0:
                time.sleep(2)
                print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
            case 1:
                score += 1
                time.sleep(2)
                print (f"Parece que {str(both_index)} esta en la posicion correcta!!")
                print ("+ (1) punto")
            case _:
                for _ in both_index:
                    score += 1
                time.sleep(2)
                print (f"Parece que {str(both_index)} estan en la posicion correcta!!")
                print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
                print (f"+ ({len(both_index)}) puntos")

    if all(flagT) == True:
        flag = True 
    else:
        flag = False 
    return score, flag

# Crea una lista de los caracteres que coinciden en ambas listas
def compare_exist(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    flagT : list = []
    in_both = []
    for char in user_chain:
        if char in org_chain:
            in_both.append(char)
        else:
            pass
        
    if len(in_both) == len(org_chain):
        flagT.append(True) 
    else:
        flagT.append(False) 
        match len(in_both):
            case 0:
                time.sleep(2)
                print("No le atinaste ni a una (ㆆ_ㆆ)")
            case 1:
                score += 1
                time.sleep(2)
                print (f"Parece que {str(in_both)} esta en la cadena!!")
                print ("+ (1) punto")
            case _:
                for _ in in_both:
                    score += 1
                time.sleep(2)
                print("( ͠❛ ₒ͠❛ ) ¿¿¿¿Te llamas Akinator????")
                print (f"Parece que {str(in_both)} estan en la cadena!!")
                print (f"+ ({len(in_both)}) puntos")

    if all(flagT) == True:
        flag = True 
    else:
        flag = False 
    return score, flag

def game_start(configuration:dict) -> bool:
    game_cont = False
    penalty : int = 0
    score : int = 0

    print("\n...Bienvenido a...")
    print("""┏━━━━━━━━━━━━━━━━━┓\n♡   R4nd.M1n1ng   ♡\n┗━━━━━━━━━━━━━━━━━┛""")
    print("Vamos a crear una cadena aleatorea y luego adivinarla")

    name = input("¿Como te llamas?: ")
    print(f"¿List@ para divertirte {name}? :D") # Guarda el user de la partida 
    print("Te hare 4-5 preguntas →")

    # Se llama a la configuración del juego que va a crear el diccionario con los datos de la partida
    start = configuration_game(configuration) 
    print(f"\n{start}") # Imprime las condiciones de cadena que esta formateado con tabulate
    
    # Crea el string aleatorio segun las configuracions del juego
    org_chain = random_combination(configuration)
    print(org_chain) # Esto no deberia aparecer en el juego pero sirve de validacion

    # "Esconden" los valores de la cadena imprimiendo * por cada caracter
    hiden_chain = "*" * len(org_chain) 
    print(f"\nIntenta adivinar ╰( ͡° ͜ʖ ͡° )つ──☆ {hiden_chain}")

    # Utiliza el estring creado por aletaorio, y se vuelve una lista que contiene sus caracteres 
    l_original = strToList(org_chain)

    # Inicializa la string del user
    user_chain = input("Ingresa tu secuencia de inicio: ")
    l_user = strToList(user_chain) # Convierte en lista la string del user 
    score = compareLengths(l_original, l_user) # Inicializa el puntaje del juego
    flag : bool = validate(user_chain, configuration) # Iniciliza la flag que permite o no el inicio del juego
    
    if score == -1 and flag == False:
        penalty = score 
        print ("Revisa bien la configuracion con la que estas jugando:")
        print(f"\n{start}")
        loading(". . .")
        print ("¿Ya?")
        user_chain = input("Ingresa la secuencia de inicio de nuevo, esta vez hazlo bien. (乛-乛)")
        l_user = strToList(user_chain)
        score = compareLengths(l_original, l_user)
        flag = validate(user_chain, configuration)
    
        if score == -1 and flag == False:
            print("GAME OVER, POR FEA")
            game_cont = False
        else:
            game_cont = True
    elif score == 0 and flag == True:
        game_cont = True
        if penalty != 0:
            score += penalty

    return user_chain, org_chain, score, l_original, l_user, game_cont

def det_score(configuration:dict, user_chain, org_chain, score, l_original, l_user, win:list) -> list:
    print("\n" + " ♥INICIA PARTIDA （*＾ワ＾*)♥ ".center(106, "~"))
    if configuration.get("Lifes") == "infinitos":
        if configuration.get("Data") == "letras":
            match configuration.get("Capital"):
                case "ambas":
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]

                    tuplaExist = compare_exist(user_chain, org_chain, score)
                    score += tuplaExist[0]
                    flagExist = tuplaExist[1]

                    tuplaIndex = compare_index(user_chain, org_chain, score)
                    score += tuplaIndex[0]
                    flagIndex = tuplaIndex[1]

                    if flagCap and flagExist and flagIndex:
                        win.append(True)
                        print("Correcto")
                    else:
                        win.append(False)
                        print("Estas equivocado")
    print(win)
    return win

if __name__ == "__main__":
    win : list = [] # Inicializa la bandera bool que contiene si el jugador ha ganado o no
    configuration : dict = {} # Guarda la configuracion de juego
    user_tries = [] # Guarda el leaderboard

    # Bucle para permitir al usuario jugar varias veces
    play_again = True
    while play_again:
        user_chain, org_chain, score, l_original, l_user, first = game_start(configuration)
        if first == True:
            second = det_score(configuration, user_chain, org_chain, score, l_original, l_user, win)
            if all(second):
                print("Ganaste")
                break
            else:
                print("Perdiste A")
        else:
            print("Perdiste B")
            break