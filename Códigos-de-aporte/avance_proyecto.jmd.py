import random
import string
from tabulate import tabulate

def configuration_game(configuration:dict): # Pregunta al jugador como quiere jugar
    # Caracteres
    data_value = input("Tipo de caracteres (letras, numeros, ambos): ")
    configuration["Data"] = data_value

    # Capitalización
    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        capital_value = input("Capitalizacion de letras (mayusculas, minusculas, ambas): ")
        configuration["Capital"] = capital_value
    else:
        pass
    
    # Repetición
    repetition_value = input("Repetición de caracteres (si, no): ")
    configuration["Repetition"] = repetition_value
    
    # Verificación de cantidad de intentos
    while True:
        amount_value = int(input("Cantidad de caracteres (3-10): "))
        if amount_value >= 3 and amount_value <= 10:
            configuration["Amount"] = amount_value
            break
        else:
            print("Valor no permitido (3-10)")
#--------------------------------------------------------------
    # Vidas (intentos para adivinar)
    lifes_value = input("Intentos (3, 5, 10, infinitos): ")
    if lifes_value == "infinitos": 
        lifes_value = float('inf')
    else: 
        lifes_value = int(lifes_value)
    configuration["Lifes"] = lifes_value
#--------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------
def validar_entrada(usuario_input:str, configuration:dict) -> bool:
    # Verifica si la entrada del usuario contiene solo caracteres permitidos.
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

    if all(char in allowed_characters for char in usuario_input) == False: 
        return "ingresaste mal un caracter intentalo de nuevo"
    else:
        return None



if __name__ == "__main__":
    configuration = {}

    print("Bienvenido a R4nd.M1n1ng")
    print("Escoga como quiere jugar")

    start = configuration_game(configuration)
    org_chain = combinacion_aleatorea(configuration)
    hiden_chain = "*" * len(org_chain)

    print(f"\n{start}")
    print(org_chain)
    print(hiden_chain)
    user_input = input("Ingresa tu intento: ")