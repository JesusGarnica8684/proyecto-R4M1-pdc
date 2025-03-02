import random
import string
from tabulate import tabulate

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

