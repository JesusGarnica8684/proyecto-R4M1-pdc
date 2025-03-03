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
        #se llama a la configuración del juego que va a crear el diccionario con los datos de la partida
        start = configuration_defs.configuration_game(configuration) 
        print(f"\n{start}") #se imprime el start que esta formateado con tabulate y se le muestra al usuario
        #se crea el string aleatorio segun las configuracions del juego
        org_chain = configuration_defs.combinacion_aleatorea(configuration)
        print(org_chain)

        hiden_chain = "*" * len(org_chain) #se "esconden" los valores de la cadena imprimiendo asteriscos por cada caracter
        print(f"\nIntenta adivinar ╰( ͡° ͜ʖ ͡° )つ──☆ {hiden_chain}")

        #se utiliza el estring creado por aletaorio, y se vuelve una lista que contiene sus caracteres 
        l_original = functionality_defs.strToList(org_chain)
        #inicializa la string del user 
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

        elif score == 0 and flag == True:
            if penalty != 0:
                score += penalty
            print("\n" + " ♥INICIA PARTIDA （*＾ワ＾*)♥ ".center(106, "~"))
            
        if configuration.get("Lifes") == "infinitos":
            match configuration.values():
                case {"Data": "letras", "Capital": "ambas"}:
                    while not win:
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

                case {"Data": "ambos", "Capital": "ambas"}:
                    while not win:
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

                case {"Data": "ambos", "Capital": "minusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  

                case {"Data": "ambos", "Capital": "mayusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  

                case {"Data": "letras", "Capital": "mayusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  

                case {"Data": "letras", "Capital": "minusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  

                case {"Data": "numeros"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  

        elif configuration.get("Lifes") in {3, 5, 10}:
            lifes = configuration.get("Lifes")
            match configuration.values():
                case {"Data": "letras", "Capital": "ambas"}:
                    while not win and lifes > 0:
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

                case {"Data": "ambos", "Capital": "ambas"}:
                    while not win and lifes > 0:
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
                
                case {"Data": "ambos", "Capital": "minusculas"}:
                    while not win and lifes > 0:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  
                        else:
                            lifes -= 1
                            if lifes == 0:
                                print("GAME OVER")
                                break    

                case {"Data": "ambos", "Capital": "mayusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  
                        else:
                            lifes -= 1
                            if lifes == 0:
                                print("GAME OVER")
                                break 

                case {"Data": "letras", "Capital": "mayusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  
                        else:
                            lifes -= 1
                            if lifes == 0:
                                print("GAME OVER")
                                break 

                case {"Data": "letras", "Capital": "minusculas"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  
                        else:
                            lifes -= 1
                            if lifes == 0:
                                print("GAME OVER")
                                break   

                case {"Data": "numeros"}:
                    while not win:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaExist[0]
                        flagExist = tuplaExist[1]

                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaIndex[0]
                        flagIndex = tuplaIndex[1]

                        if flagExist and flagIndex:
                            win = True  
                        else:
                            lifes -= 1
                            if lifes == 0:
                                print("GAME OVER")
                                break 



                        

#-------------------------------------------------------------------------
            elif win == True:
                functionality_defs.cargando("GANASTEEEEEEEEEEEEEEEEE")
            elif win == False:
                functionality_defs.cargando("PERDISTEEEEEEEEEEEEEEEEE")

            # Al terminar la partida, pregunta al usuario si quiero jugar otravez
            dead = input("¿Quieres jugar otra vez?: ")
            if dead == "si":
                functionality_defs.history("\n", name, score) # Mostrar leaderboard
            elif dead == "no":
                break
    functionality_defs.history("\n", name, score)
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━┓\n♡   Gracias por jugar   ♡\n┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
    #-------------------------------------------------------------------------
