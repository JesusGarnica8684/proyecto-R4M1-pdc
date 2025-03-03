from tabulate import tabulate
import time 
import configuration_defs
import functionality_defs
import score_defs

if __name__ == "__main__":
    configuration : dict = {} # Guarda la configuracion de juego
    user_tries = [] # Guarda el leaderboard

    # Bucle para permitir al usuario jugar varias veces
    while True:
        print("\n...Bienvenido a...")
        print("""┏━━━━━━━━━━━━━━━━━┓\n♡   R4nd.M1n1ng   ♡\n┗━━━━━━━━━━━━━━━━━┛""")
        name = input("¿Como te llamas?: ")
        print(f"¿List@ para divertirte {name}? :D") #Guarda el user de la partida 
        print("Te hare 5 preguntas →")
        
        # Configuración del juego
        start = configuration_defs.configuration_game(configuration) 
        print(f"\n{start}") #se imprime el start que esta formateado con tabulate y se le muestra al usuario
        
        # Crear la cadena aleatoria según las configuraciones del juego
        org_chain = configuration_defs.combinacion_aleatorea(configuration)
        print(org_chain)

        hiden_chain = "*" * len(org_chain) #se "esconden" los valores de la cadena imprimiendo asteriscos por cada caracter
        print(f"\nIntenta adivinar ╰( ͡° ͜ʖ ͡° )つ──☆ {hiden_chain}")

        # Convertir la cadena original en una lista
        l_original = functionality_defs.strToList(org_chain)
        
        # Inicializar la cadena del usuario
        user_chain = input("Ingresa tu secuencia de inicio: ")
        l_user = functionality_defs.strToList(user_chain) # se convierte en lista la string del user 
        score : int = score_defs.compareLengths(l_original, l_user) # se inicializa el puntaje del juego
        penalty : int = 0 
        flag : bool = functionality_defs.validar_entrada(user_chain, configuration) # se iniciliza la flag que permite o no el inicio del juego
        win : bool = False # se inicializa la bandera bool que contiene si el jugador ha ganado o no
        
        if score == -1 and flag == False:
            penalty = score 
            print ("Revisa bien la configuracion con la que estas jugando:")
            print(f"\n{start}")
            functionality_defs.cargando (". . .")
            print ("¿Ya?")
            user_chain = input("Ingresa la secuencia de inicio de nuevo, esta vez hazlo bien. (乛-乛)")
            l_user = functionality_defs.strToList(user_chain)
            score = score_defs.compareLengths(l_original, l_user)
            flag = functionality_defs.validar_entrada(user_chain, configuration)
        elif score == -1 and flag == False:
            print ("GAME OVER, POR FEA")
            continue  # Volver al inicio del bucle principal

        elif score == 0 and flag == True:
            if penalty != 0:
                score += penalty
            print("\n" + " ♥INICIA PARTIDA （*＾ワ＾*)♥ ".center(106, "~"))
            
        # Configuración de vidas infinitas
        if configuration.get("Lifes") == "infinitos":
            again : int = 0
            while not win:
                if configuration.get("Data") == "letras" and configuration.get("Capital") == "ambas":
                    tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]

                    tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                    score += tuplaExist[0]
                    flagExist = tuplaExist[1]

                    tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                    score += tuplaIndex[0]
                    flagIndex = tuplaIndex[1]

                    if flagCap and flagExist and flagIndex:
                        win = True
                    else:
                        user_chain = input("Intenta de nuevo: ")
                        l_user = functionality_defs.strToList(user_chain)
                        again += 1

                # Otros casos de configuración...

        # Configuración de vidas limitadas
        elif configuration.get("Lifes") in {3, 5, 10}:
            lifes = configuration.get("Lifes")
            while not win and lifes > 0:
                if configuration.get("Data") == "letras" and configuration.get("Capital") == "ambas":
                    tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]

                    tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                    score += tuplaExist[0]
                    flagExist = tuplaExist[1]

                    tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                    score += tuplaIndex[0]
                    flagIndex = tuplaIndex[1]

                    if flagCap and flagExist and flagIndex:
                        win = True
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print("GAME OVER")
                            break
                        user_chain = input(f"Intenta de nuevo. Te quedan {lifes} vidas: ")
                        l_user = functionality_defs.strToList(user_chain)

                # Otros casos de configuración...

        if win:
            functionality_defs.cargando("GANASTEEEEEEEEEEEEEEEEE")
            print(f"¡Felicidades {name}! Has ganado con un puntaje de {score}.")

        # Al terminar la partida, pregunta al usuario si quiere jugar otra vez
        dead = input("¿Quieres jugar otra vez? (si/no): ")
        if dead == "no":
            break

    functionality_defs.history("\n", name, score)
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━┓\n♡   Gracias por jugar   ♡\n┗━━━━━━━━━━━━━━━━━━━━━━━┛""")