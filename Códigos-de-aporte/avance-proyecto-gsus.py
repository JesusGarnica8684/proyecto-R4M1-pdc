import random
import string
from tabulate import tabulate
import time 

#Def print de carga, for a dramatic flare 

def cargando(text: str):
    for i in text: # recorre cada caracter del string
        print(i, end="") # va imprimiendolo uno por uno conforme avanza
        time.sleep(0.2) # retrasa la siguiente accion 2 decimas de segundo

#Def string a lista (va a utilizarse tanto para lista con la respuesta como la que ingresar el usuario) 
def strToList (secuencia : str) -> list:
    return list(secuencia)

#Def comparar lista- respuesta con lista-usuario (se revisa que las dos sean iguales de largas, sino, se resta 1 punto)
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
        
#Def comparar mayusculas minúsculas de las listas
def compareCapnoCap (listR: list, listU : list) -> int:
    score : int = 0
    capU : list = []
    noCapU : list = []
    for i in listU:
        if i.isalpha() and i.isupper():  # Verificar si el carácter es alfabético y mayúscula
            capU.append(i)
        elif i.isalpha() and i.islower():  # Verificar si el carácter es alfabético y minúscula
            noCapU.append(i) 
    for i in listR:
        if i in capU and i in noCapU:
            score += 2
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista tanto en mayuscula como minuscula")
            print ("Un piko por inteliegente ( ˘ ³˘)♥")
            print ("(+2) puntos")
        elif i in capU and i not in noCapU:
            score += 1
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista en mayuscula pero no en minuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        elif i not in capU and i in noCapU:
            score += 1
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista en minuscula pero no en mayuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        else:  
            time.sleep(2)
            cargando ("Ah dale, obvio, claro, claro (•ิ _•ิ )...")  
    return score  

def validar_entrada(usuario_input:str, configuration:dict) -> bool:
    #Verifica si la entrada del usuario contiene solo caracteres permitidos.
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

def comparar_existencia(usuario_input:str, org_chain:str) -> list:
    #Crea una lista de los caracteres que coinciden en ambas listas.
    return [char for char in set(usuario_input) if char in org_chain]

def comparar_indice_aparicion(usuario_input:str, org_chain:str) -> dict:
    #Crea un diccionario con los caracteres que coinciden en posicion.
    indices = {}
    for char in set(usuario_input):
        if char in org_chain:
            indices[char] = [i for i, c in enumerate(org_chain) if c == char]
    return indices

def configuration_game(configuration:dict): # Pregunta al jugador como quiere jugar
    # Caracteres
    data_value = input("    1- Tipo de caracteres (letras, numeros, ambos): ")
    configuration["Data"] = data_value

    # Capitalización
    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        capital_value = input("    2- Capitalizacion de letras (mayusculas, minusculas, ambas): ")
        configuration["Capital"] = capital_value
    else:
        pass
    
    # Repetición
    repetition_value = input("    3- Repetición de caracteres (si, no): ")
    configuration["Repetition"] = repetition_value
    
    # Verificación de cantidad de intentos
    while True:
        amount_value = int(input("    4- Cantidad de caracteres (3-10): "))
        if amount_value >= 3 and amount_value <= 10:
            configuration["Amount"] = amount_value
            break
        else:
            print("Te dije que 3 a 10 . _.)")

    # Vidas (intentos para adivinar)
    lifes_value = input("    5- Intentos (3, 5, 10, infinitos): ")
    if lifes_value == "infinitos": 
        lifes_value = float('inf')
    else: 
        lifes_value = int(lifes_value)
    configuration["Lifes"] = lifes_value

    # Imprimir el diccionario en forma de tabla
    configuration_tab = tabulate(configuration.items(), tablefmt= "grid")

    return configuration_tab

def combinacion_aleatorea(configuration:dict):
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

if __name__ == "__main__":
    configuration = {}

    print("\n...Bienvenido a...")
    print("""┏━━━━━━━━━━━━━━━━━┓\n♡   R4nd.M1n1ng   ♡\n┗━━━━━━━━━━━━━━━━━┛""")
    print("¿Listo para divertirte? :D")
    print("Te hare 5 preguntas →")
    cargando("Cargando partida... (づ๑•ᴗ•๑)づ♡ <(⸝⸝ᵕᴗᵕ⸝⸝<) \n")

    start = configuration_game(configuration)
    print(f"\n{start}")

    org_chain = combinacion_aleatorea(configuration)
    print(org_chain)

    hiden_chain = "*" * len(org_chain)
    print(hiden_chain)
    
    l_original = strToList(org_chain)
    user_chain = input("Ingresa tu secuencia de inicio: ")
    l_user = strToList(user_chain)
    score : int = compareLengths(l_original, l_user)
    flag : bool = validar_entrada(user_chain, configuration)
    
    if score == -1 and flag == False:
        print ("Revisa bien la configuracion con la que estas jugando:")
        print(f"\n{start}")
        cargando (". . .")
        print ("¿Ya?")
        user_chain = input("Ingresa la secuencia de inicio de nuevo, esta vez hazlo bien. (乛-乛)")
        l_user = strToList(user_chain)
        score : int = -1
    elif score == -1 and flag == False:
        print ("GAME OVER, POR FEA")
    elif score == 0:
        print("\nINICIA PARTIDA （*＾ワ＾*）".center(" "))
        if {"Lifes":"infinitos"}:
            match configuration.values():
                case {"Data":"letras", "Repetition":"si", "Capital":"ambas"}:
                    score += compareCapnoCap(l_original, l_user)
        if {"Lifes":3} or {"Lifes":5} or {"Lifes":10}:
            match configuration.values():
                case {"Data":"letras", "Repetition":"si", "Capital":"ambas"}:
                    score += compareCapnoCap(l_original, l_user)
                    




        


