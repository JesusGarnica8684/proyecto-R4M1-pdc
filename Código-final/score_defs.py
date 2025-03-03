import random
import string
from tabulate import tabulate
import time 
import functionality_defs

# Comparar lista-respuesta con lista-usuario (Revisa que las dos sean iguales de largas)
def compareLengths (listR, listU : list) -> int:
    score : int = 0
    if len(listR) == len(listU):
        score = 0
        print("LGFG!!! Son del mismo largo (づ ◕‿◕ )づ")
    elif len(listR) > len(listU):
        score = -1
        print("Tch!!! la secuencia es mas larga de lo que ingresaste")
        time.sleep(2)
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        time.sleep(2)
        functionality_defs.cargando("(-1) punto, por atembao") 
    else: 
        score = -1
        print("Tch!!! la secuencia es mas corta de lo que ingresaste")
        time.sleep(2)
        print("¿No recuerdas como configuraste la partida? (乛-乛)")
        time.sleep(2)
        functionality_defs.cargando("(-1) punto, por atembao") 
    return score

#! Comparar mayusculas minúsculas de las listas
def compareCapnoCap (listR: list, listU : list) -> tuple[int, bool]:
    score : int = 0
    capU : list = []
    noCapU : list = []
    flagT : tuple = ()
    for i in listU:
        if i.isalpha() and i.isupper(): # Verificar si el carácter es alfabético y mayúscula
            capU.append(i)
        elif i.isalpha() and i.islower(): # Verificar si el carácter es alfabético y minúscula
            noCapU.append(i) 
    for i in listR:
        if i in capU and i in noCapU:
            score += 2
            flagT.append(True) 
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista tanto en mayuscula como minuscula")
            print ("Un piko por inteliegente ( ˘ ³˘)♥")
            print ("(+2) puntos")
        elif i in capU and i not in noCapU:
            score += 1
            flagT.append(False) 
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista en mayuscula pero no en minuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        elif i not in capU and i in noCapU:
            score += 1
            flagT.append(False) 
            time.sleep(2)
            print (f"Oh! parece que {i} si se encuentra en la lista en minuscula pero no en mayuscula")
            print ("A la proxima hazlo mejor, ok? (˶ ⚈ Ɛ ⚈ ˵)")
            print ("(+1) punto")
        else:  
            time.sleep(2)
            functionality_defs.cargando ("Ah dale, obvio, claro, claro (•ิ _•ิ )...")  
    if all.flagT() == True:
        flag = True 
    else:
        flag = False 
    return score, flag  

#! Crea una lista con los caracteres que coinciden en posicion
def compare_index(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    both_index = []
    bot = zip(org_chain, user_chain)
    both = list(bot)
    for org, user in both:
        if org == user:
            both_index.append(user)
        else:
            pass 

    match len(both_index):
        case 0:
            print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
        case 1:
            score += 1
            print (f"Parece que {str(both_index)} esta en la posicion correcta!!")
            print ("+ (1) punto")
        case _:
            for _ in both_index:
                score += 1
            print (f"Parece que {str(both_index)} estan en la posicion correcta!!")
            print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
            print (f"+ ({len(both_index)}) puntos")
    return score, flag

#! Crea una lista de los caracteres que coinciden en ambas listas
def compare_exist(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    flagT : tuple = ()
    in_both = []
    for char in user_chain:
        if char in org_chain:
            in_both.append(char)
        else:
            pass

    match len(in_both):
        case 0:
            print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
        case 1:
            score += 1
            print (f"Parece que {str(in_both)} esta en la cadena!!")
            print ("+ (1) punto")
        case _:
            for _ in in_both:
                score += 1
            print (f"Parece que {str(in_both)} estan en la cadena!!")
            print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
            print (f"+ ({len(in_both)}) puntos")

    if all.flagT() == True:
        flag = True 
    else:
        flag = False 
    return score, flag 
