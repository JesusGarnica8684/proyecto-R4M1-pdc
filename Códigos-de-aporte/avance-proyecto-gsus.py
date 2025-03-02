#Def string a lista (va a utilizarse tanto para lista con la respuesta como la que ingresar el usuario) 
def strToList (secuencia : str) -> list:
    return list(secuencia)

#Def comparar lista- respuesta con lista-usuario (se revisa que las dos sean iguales de largas, sino, se resta 1 punto)
def compareLengths (listR, listU : list) -> int:
    score : int = 0
    if len(listR) == len(listU):
        score = 0
        print("LGFG!!! Son del mismo largo (づ ◕‿◕ )づ")
    elif len(listR) >= len(listU):
        score = -1
        print("Tch!!! la secuencia es mas larga de lo que ingresaste")
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        print("Menos (1) punto, por atembao") 
    else: 
        score = -1
        print("Tch!!! la secuencia es mas corta de lo que ingresaste")
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        print("Menos (1) punto, por atembao") 
    return score
        
#Def comparar mayusculas minúsculas de las listas
def compareCapnoCap (strR: str, strU: str, listR: list, listU: list) -> int:
    score : int = 0
    capU: list = strU.isalpha(strU.isupper())
    noCapU: list = strU.isalpha(strU.islower())
    for i in listR:
        if i in capU: 
            if i in noCapU:
                score += 2
                print (f"Oh! parece que {listR[i]} si se encuentra en la lista tanto en mayuscula como minuscula")
                print ("Un piko por inteliegente ( ˘ ³˘)♥")
                print ("Mas (2) puntos")
        elif i in capU: 
            if i not in noCapU:
                score += 1
                print (f"Oh! parece que {listR[i]} si se encuentra en la lista en mayuscula pero no en minuscula")
                print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
                print ("Mas (1) punto")
        elif i not in capU: 
            if i in noCapU:
                score += 1
                print (f"Oh! parece que {listR[i]} si se encuentra en la lista en minuscula pero no en mayuscula")
                print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
                print ("Mas (1) punto")
        else:  
            print ("Ah dale, obvio, claro (•ิ _•ิ ).")  
    return score  

