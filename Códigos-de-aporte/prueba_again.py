again : int = 0
if flagCap and flagExist and flagIndex:
    win = True
else:
    while True:
        for i in range(10):                          
            quest = input("¿Quieres seguir jugando?")
            if quest == "no":
                break
            elif quest == "si":
                win = False
        again += 1
