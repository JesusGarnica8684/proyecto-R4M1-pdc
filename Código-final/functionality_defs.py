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
