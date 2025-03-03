from tabulate import tabulate


def game(name:str, score:int):
    win : bool = False
    if name and score:
        win == True
    if win == True:
        history(name, score)
    return win

def history(user_tries:list, name:str, score:int) -> dict:
    partida = {
        "Nombre" : name,
        "Puntaje" : score
    }
    user_tries.append(partida)
    sorted(user_tries, reverse= True)

    rank : int = 1
    for dic in user_tries:
        dic["rank"] = rank
        rank += 1

    # Imprimir el diccionario en forma de tabla
    user_tries_tab = tabulate(user_tries, headers= "keys", tablefmt= "grid")
    return user_tries_tab

if __name__ == "__main__":
    user_tries = []

    while True:
        dead : bool = False
        name = input("name: ")
        score = int(input("score: "))

        uno = game(name, score)
        q_dead = input("¿Quieres jugar otra vez?: ")

        if q_dead == "si":
            dead = False
            dos = history(user_tries, name, score)
            print(dos)
        elif q_dead == "no":
            dead = True
            break
    dos = history(name, score)
    print(dos)