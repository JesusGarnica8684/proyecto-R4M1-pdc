import random
import string
from tabulate import tabulate
import time 

# Print de carga, for a dramatic flare 
def cargando(text: str):
    for i in text: # recorre cada caracter del string
        print(i, end="") # va imprimiendolo uno por uno conforme avanza
        time.sleep(0.2) # retrasa la siguiente accion 2 decimas de segundo

# String a lista (Parar lista-respuesta y lista-usuario) 
def strToList (secuencia : str) -> list:
    return list(secuencia)

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
        cargando("(-1) punto, por atembao") 
    else: 
        score = -1
        print("Tch!!! la secuencia es mas corta de lo que ingresaste")
        time.sleep(2)
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        time.sleep(2)
        cargando("(-1) punto, por atembao") 
    return score
        
#! Comparar mayusculas minúsculas de las listas
def compareCapnoCap (listR: list, listU : list) -> tuple[int, bool]:
    score : int = 0
    capU : list = []
    noCapU : list = []
    flagT : tuple = []
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
            print (f"Oh! parece que {i} si se encuentra en la lista tanto en mayuscula como minuscula")
            print ("Un piko por inteliegente ( ˘ ³˘)♥")
            print ("(+2) puntos")
        elif i in capU and i not in noCapU:
            score += 1
            flagT.append(False) 
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista en mayuscula pero no en minuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        elif i not in capU and i in noCapU:
            score += 1
            flagT.append(False) 
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista en minuscula pero no en mayuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        else:  
            time.sleep(2)
            cargando ("Ah dale, obvio, claro, claro (•ิ _•ิ )...")  
    if all.flagT() == True:
        flag = True 
    else:
        flag = False 
    return score, flag  

# Verifica si la entrada del usuario contiene solo caracteres permitidos
def validar_entrada(usuario_input:str, configuration:dict) -> bool:
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
        cargando (". . .")
        print ("Mmm... \n")
        print ("¿No recuerdas como configuraste la partida?(ﾉಠдಠ)ﾉ︵┻━┻")
    else:
        validacion : bool = True
        cargando ("♥°˖✧°˖✧°˖✧°˖✧°˖✧◝(⁰▿⁰)◜✧˖°✧˖°✧˖°✧˖°♥")
    return validacion 

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
        if lifes_value in {3, 5, 10} or lifes_value :
            if lifes_value == "infinitos": 
                lifes_value = float('inf')
            else: 
                lifes_value = int(lifes_value)
            configuration["Lifes"] = lifes_value
            break
        else:
            print("Opcion NO disponible -(`෴´)- ")

    # Imprimir el diccionario en forma de tabla
    configuration_tab = tabulate(configuration.items(), tablefmt= "grid")

    return configuration_tab

# Genera la cadena por adivinar
def combinacion_aleatorea(configuration:dict) -> list: 
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

#! Crea una lista con los caracteres que coinciden en posicion
def compare_index(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    both_index = []
    bot = zip(org_chain, user_chain)
    both = list(bot)
    for org, user in both:
        if org == user:
            both_index.append(user)
        else:
            pass 

    match len(both_index):
        case 0:
            print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
        case 1:
            score += 1
            print (f"Parece que {str(both_index)} esta en la posicion correcta!!")
            print ("+ (1) punto")
        case _:
            for _ in both_index:
                score += 1
            print (f"Parece que {str(both_index)} estan en la posicion correcta!!")
            print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
            print (f"+ ({len(both_index)}) puntos")
    return score, flag

#! Crea una lista de los caracteres que coinciden en ambas listas
def compare_exist(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    flagT : tuple = []
    in_both = []
    for char in user_chain:
        if char in org_chain:
            in_both.append(char)
        else:
            pass

    match len(in_both):
        case 0:
            print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
        case 1:
            score += 1
            print (f"Parece que {str(in_both)} esta en la cadena!!")
            print ("+ (1) punto")
        case _:
            for _ in in_both:
                score += 1
            print (f"Parece que {str(in_both)} estan en la cadena!!")
            print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
            print (f"+ ({len(in_both)}) puntos")

    if all.flagT() == True:
        flag = True 
    else:
        flag = False 
    return score, flag 

def history(name:str, score:int) -> dict:
    user_tries = []
    partida = {
        "Nombre" : name,
        "Puntaje" : score
    }
    user_tries.append(partida)
    sorted(user_tries, reversed= True)

    rank : int = 1
    for dic in user_tries:
        dic["rank"] = rank
        rank += 1

    # Imprimir el diccionario en forma de tabla
    user_tries_tab = tabulate(user_tries, headers= "keys", tablefmt= "grid")
    return user_tries_tab

def game_start(configuration:dict):
    if configuration.get("Lifes") == "infinitos":
        match configuration.values():
            case {"Data": "letras", "Repetition": "si", "Capital": "ambas"}:
                while win == False:
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]
            case {"Data": "letras", "Repetition": "no", "Capital": "ambas"}:
                while win == False:
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]

    if configuration.get("Lifes") in {3, 5, 10}:
        match configuration.values():
            case {"Data": "letras", "Repetition": "si", "Capital": "ambas"}:
                lifes = configuration.get("Lifes")
                for _ in range(lifes):
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]
            case {"Data": "letras", "Repetition": "no", "Capital": "ambas"}:
                xxx
        if win == True:
            history(name, score)


if __name__ == "__main__":
    configuration : dict = {}

    print("\n...Bienvenido a...")
    print("""┏━━━━━━━━━━━━━━━━━┓\n♡   R4nd.M1n1ng   ♡\n┗━━━━━━━━━━━━━━━━━┛""")
    name = input("¿Como te llamas?: ")
    print(f"¿Listo para divertirte {name}? :D")
    print("Te hare 5 preguntas →")

    start = configuration_game(configuration)
    print(f"\n{start}")

    org_chain = combinacion_aleatorea(configuration)
    print(org_chain)

    hiden_chain = "*" * len(org_chain)
    print(f"\nIntenta adivinar ╰( ͡° ͜ʖ ͡° )つ──☆ {hiden_chain}")

    l_original = strToList(org_chain)
    user_chain = input("Ingresa tu secuencia de inicio: ")
    l_user = strToList(user_chain)
    score : int = compareLengths(l_original, l_user)
    penalty : int = 0
    flag : bool = validar_entrada(user_chain, configuration)
    win : bool = False
    
    if score == -1 and flag == False:
        penalty = score 
        print ("Revisa bien la configuracion con la que estas jugando:")
        print(f"\n{start}")
        cargando (". . .")
        print ("¿Ya?")
        user_chain = input("Ingresa la secuencia de inicio de nuevo, esta vez hazlo bien. (乛-乛)")
        l_user = strToList(user_chain)
        score = compareLengths(l_original, l_user)
    elif score == -1 and flag == False:
        print ("GAME OVER, POR FEA")

    elif score == 0:
        if penalty != 0:
            score += penalty
        print("\n" + " ♥INICIA PARTIDA （*＾ワ＾*)♥ ".center(106, "~"))
        game_game = game_start(configuration)

#-----------------------------------------------------------------------------------------
    while True:
        dead : bool = False
        q_dead = input("¿Quieres jugar otra vez?: ")
        if q_dead == "si":
            dead = False
        elif q_dead == "no":
            dead = True
            break

#----------------------------------------------------------------------------------------

    #user_chain = input("Ingresa tu secuencia de inicio: ")
    #play = compare_exist(user_chain, org_chain, score)
    #play_b = compare_index(user_chain, org_chain, score)