import random
import string
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
        if lifes_value in {3, 5, 10, "infinitos"}:
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

# Crea una lista con los caracteres que coinciden en posicion
def compare_index(user_chain:str, org_chain:str, score:int) -> list:
    both_index = []
    for char in user_chain:
        index = enumerate(org_chain) 
        if char in org_chain:
            for i, c in index:
                if c == char:
                    both_index.append(i)
    for _ in both_index:
        score += 1
    return both_index

# Crea una lista de los caracteres que coinciden en ambas listas
def compare_exist(user_chain:str, org_chain:str, score:int) -> list:
    in_both = []
    for char in user_chain:
        if char in org_chain:
            in_both.append(char)

    if not in_both: # Si la lista esta vacia
        print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
    elif len(in_both) >= 3:
        print (f"Parece que {str(in_both)} estan en la posicion correcta!!")
        print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
        print ("+ (2) punto")
    elif len(in_both) == 1:
        print (f"Parece que {str(in_both)} esta en la posicion correcta!!")
        print ("+ (1) punto")
    
    return in_both

if __name__ == "__main__":
    configuration = {}
    score: int = 0

    print("\n...Bienvenido a...")
    print("""┏━━━━━━━━━━━━━━━━━┓\n♡   R4nd.M1n1ng   ♡\n┗━━━━━━━━━━━━━━━━━┛""")
    print("¿Listo para divertirte? :D")
    print("Te hare 5 preguntas →")

    start = configuration_game(configuration)
    print(f"\n{start}")

    org_chain = combinacion_aleatorea(configuration)
    print(org_chain)

    hiden_chain = "*" * len(org_chain)
    print(f"\nIntenta adivinar ╰( ͡° ͜ʖ ͡° )つ──☆ {hiden_chain}")

    user_chain = input("Ingresa tu secuencia de inicio: ")
