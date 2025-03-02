#Def string a lista (va a utilizarse tanto para lista con la respuesta como la que ingresar el usuario) 
def strToList (secuencia : str) -> list:
    return list(secuencia)
#Def comparar lista- respuesta con lista-usuario (se revisa que las dos sean iguales de largas, sino, se resta 1 punto)
def compareLengths (listR, listU : list) -> int:
    score : int = 0
    if len(listR) == len(listU):
        score = 1
        print("LGFG!!! Son del mismo largo (づ ◕‿◕ )づ")
    elif len(listR) >= len(listU):
        score = 0
        print("Tch!!! la secuencia es mas larga de lo que ingresaste")
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
    return score
        
#Def comparar mayusculas minúsculas de las listas
def compareCapnoCap (list1, list2 : list) -> int: