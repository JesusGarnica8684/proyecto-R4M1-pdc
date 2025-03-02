import random
import string
from tabulate import tabulate

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
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        print("(-1) punto, por atembao") 
    else: 
        score = -1
        print("Tch!!! la secuencia es mas corta de lo que ingresaste")
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        print("(-1) punto, por atembao") 
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
            print (f"Oh! parece que {i} si se encuentra en la lista tanto en mayuscula como minuscula")
            print ("Un piko por inteliegente ( ˘ ³˘)♥")
            print ("(+2) puntos")
        elif i in capU and i not in noCapU:
            score += 1
            print (f"Oh! parece que {i} si se encuentra en la lista en mayuscula pero no en minuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        elif i not in capU and i in noCapU:
            score += 1
            print (f"Oh! parece que {i} si se encuentra en la lista en minuscula pero no en mayuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        else:  
            print ("Ah dale, obvio, claro, claro (•ิ _•ิ ).")  
    return score  

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
    
    if score == -1:
        print ("Revisa bien cuantos caracteres estas jugando con:")
        print(f"\n{start} \n¿Listo?")
        user_chain = input("Ingresa la secuencia de inicio de nuevo, esta vez hazlo bien. (乛-乛)")
        l_user = strToList(user_chain)
        score : int = -1
    elif score == -1:
        print ("GAME OVER, POR FEA")
    elif score == 0:
        print ("INICIA PARTIDA （*＾ワ＾*）")
        score += compareCapnoCap(l_original, l_user)



        


