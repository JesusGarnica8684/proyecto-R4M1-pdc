import random
import string
import tabulate

def configuration_game(configuration:dict): # Pregunta al jugador como quiere jugar
    data_value = input("Tipo de caracteres (letras, numeros, ambos): ")
    configuration["Data"] = data_value

    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        capital_value = input("Capitalizacion de letras (mayusculas, minusculas, ambas): ")
        configuration["Capital"] = capital_value
    else:
        pass

    repetition_value = input("Repetición de caracteres (si, no): ")
    configuration["Repetition"] = repetition_value

    while True: # Verificación de cantidad de intentos
        amount_value = int(input("Cantidad de caracteres (3-10): "))
        if amount_value >= 3 and amount_value <= 10:
            configuration["Amount"] = amount_value
            break
        else:
            print("Valor no permitido (3-10)")

    lifes_value = input("Intentos (3, 5, 10, infinitos): ")
    configuration["Lifes"] = lifes_value

    return configuration

def combinacion_aleatorea(configuration:dict):
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

    if configuration["Repetition"] == "no":
        chain = "".join(random.sample(options_string, lon))
    else:
        chain = "".join(random.choices(options_string, k = lon))
        
    return chain

if __name__ == "__main__":
    configuration = {}

    start = configuration_game(configuration)
    org_chain = combinacion_aleatorea(configuration)
    hiden_chain = "*" * len(org_chain)

    print("Bienvenido a R4nd.M1n1ng")
    print(start)
    print(org_chain)
    print(hiden_chain)