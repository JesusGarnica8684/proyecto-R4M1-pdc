from tabulate import tabulate
import time 
import configuration_defs
import functionality_defs
import score_defs

if __name__ == "__main__":
    configuration : dict = {}

    print("\n...Bienvenido a...")
    print("""┏━━━━━━━━━━━━━━━━━┓\n♡   R4nd.M1n1ng   ♡\n┗━━━━━━━━━━━━━━━━━┛""")
    name = input("¿Como te llamas?: ")
    print(f"¿Listo para divertirte {name}? :D")
    print("Te hare 5 preguntas →")

    start = configuration_defs.configuration_game(configuration)
    print(f"\n{start}")

    org_chain = configuration_defs.combinacion_aleatorea(configuration)
    print(org_chain)

    hiden_chain = "*" * len(org_chain)
    print(f"\nIntenta adivinar ╰( ͡° ͜ʖ ͡° )つ──☆ {hiden_chain}")

    l_original = functionality_defs.strToList(org_chain)
    user_chain = input("Ingresa tu secuencia de inicio: ")
    l_user = functionality_defs.strToList(user_chain)
    score : int = score_defs.compareLengths(l_original, l_user)
    penalty : int = 0
    flag : bool = functionality_defs.validar_entrada(user_chain, configuration)
    win : bool = False
    
    if score == -1 and flag == False:
        penalty = score 
        print ("Revisa bien la configuracion con la que estas jugando:")
        print(f"\n{start}")
        functionality_defs.cargando (". . .")
        print ("¿Ya?")
        user_chain = input("Ingresa la secuencia de inicio de nuevo, esta vez hazlo bien. (乛-乛)")
        l_user = functionality_defs.strToList(user_chain)
        score = score_defs.compareLengths(l_original, l_user)
    elif score == -1 and flag == False:
        print ("GAME OVER, POR FEA")

    elif score == 0:
        if penalty != 0:
            score += penalty
        print("\n" + " ♥INICIA PARTIDA （*＾ワ＾*)♥ ".center(106, "~"))
        
        if configuration.get("Lifes") == "infinitos":
            match configuration.values():
                case {"Data": "letras", "Repetition": "si", "Capital": "ambas"}:
                    while win == False:
                        tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                        score += tuplaCapnoCap(0)
                        flagCap = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"Data": "letras", "Repetition": "no", "Capital": "ambas"}:
                    while win == False:
                        tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                        score += tuplaCapnoCap(0)
                        flagCap = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"Data": "ambos", "Repetition": "no", "Capital": "ambas"}:
                    while win == False:
                        tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                        score += tuplaCapnoCap(0)
                        flagCap = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"Data": "ambos", "Repetition": "si", "Capital": "ambas"}:
                    while win == False:
                        tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                        score += tuplaCapnoCap(0)
                        flagCap = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"Data": "ambos", "Repetition": "no", "Capital": "minusculas"}:
                    while win == False:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"Data": "ambos", "Repetition": "si", "Capital": "mayusculas"}:
                    while win == False:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"letras": "ambos", "Repetition": "no", "Capital": "minusculas"}:
                    while win == False:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
                case {"Data": "letras", "Repetition": "si", "Capital": "mayusculas"}:
                    while win == False:
                        tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagExist = tuplaCapnoCap[1]
                        time.sleep(2)
                        tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                        score += tuplaCapnoCap(0)
                        flagIndex = tuplaCapnoCap[1]
                        if flagCap and flagExist and flagIndex == True:
                            win = True 
                        else: 
                            win = False
                            time.sleep(2) 
        elif configuration.get("Lifes") in {3, 5, 10}:
            match configuration.values():
                case {"Data": "letras", "Repetition": "si", "Capital": "ambas"}:
                    lifes = configuration.get("Lifes")
                    for _ in range(lifes):
                        while win == False:
                            tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                            score += tuplaCapnoCap(0)
                            flagCap = tuplaCapnoCap[1]
                            tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagExist = tuplaCapnoCap[1]
                            tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagIndex = tuplaCapnoCap[1]
                            if flagCap and flagExist and flagIndex == True:
                                win = True 
                            else: 
                                win = False 
                case {"Data": "letras", "Repetition": "no", "Capital": "ambas"}:
                    lifes = configuration.get("Lifes")
                    for _ in range(lifes):
                            tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                            score += tuplaCapnoCap(0)
                            flagCap = tuplaCapnoCap[1]
                            tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagExist = tuplaCapnoCap[1]
                            tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagIndex = tuplaCapnoCap[1]
                            if flagCap and flagExist and flagIndex == True:
                                win = True 
                            else: 
                                win = False 
                case {"Data": "ambas", "Repetition": "si", "Capital": "ambas"}:
                    lifes = configuration.get("Lifes")
                    for _ in range(lifes):
                            tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                            score += tuplaCapnoCap(0)
                            flagCap = tuplaCapnoCap[1]
                            tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagExist = tuplaCapnoCap[1]
                            tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagIndex = tuplaCapnoCap[1]
                            if flagCap and flagExist and flagIndex == True:
                                win = True 
                            else: 
                                win = False 
                case {"Data": "ambas", "Repetition": "no", "Capital": "ambas"}:
                    lifes = configuration.get("Lifes")
                    for _ in range(lifes):
                            tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                            score += tuplaCapnoCap(0)
                            flagCap = tuplaCapnoCap[1]
                            tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagExist = tuplaCapnoCap[1]
                            tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagIndex = tuplaCapnoCap[1]
                            if flagCap and flagExist and flagIndex == True:
                                win = True 
                            else: 
                                win = False 
                case {"Data": "ambas", "Repetition": "si", "Capital": "ambas"}:
                    lifes = configuration.get("Lifes")
                    for _ in range(lifes):
                            tuplaCapnoCap = score_defs.compareCapnoCap(l_original, l_user)
                            score += tuplaCapnoCap(0)
                            flagCap = tuplaCapnoCap[1]
                            tuplaExist = score_defs.compare_exist(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagExist = tuplaCapnoCap[1]
                            tuplaIndex = score_defs.compare_index(user_chain, org_chain, score)
                            score += tuplaCapnoCap(0)
                            flagIndex = tuplaCapnoCap[1]
                            if flagCap and flagExist and flagIndex == True:
                                win = True 
                            else: 
                                win = False 
        elif win == True:
            functionality_defs.history(name, score)
#-----------------------------------------------------------------------------------------
    while True:
        dead : bool = False
        q_dead = input("¿Quieres jugar otra vez?: ")
        if q_dead == "si":
            dead = False
        elif q_dead == "no":
            dead = True
            break

#----------------------------------------------------------------------------------------

    #user_chain = input("Ingresa tu secuencia de inicio: ")
    #play = compare_exist(user_chain, org_chain, score)
    #play_b = compare_index(user_chain, org_chain, score)