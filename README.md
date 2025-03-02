# **R4nd.M1n1ng**
***
## Un proyecto de Cobra Kode
![](Logo/logo-cobra-kode.png)
## Introduccion 
El siguiente repositorio describe el desarrollo e implementación de **R4nd.M1n1ng**, un juego que consiste en la generación y adivinanza de una serie de caracteres aleatorios. El objetivo es que el usuario descubra la secuencia oculta mediante intentos sucesivos y un sistema de puntuación.
***
## Cómo se abordó el problema
Se desarrolló el código del juego con una estructura de funciones específicas. A continuación, se presenta cada una de ellas y su propósito dentro del juego: 

### Funciones de utilidades 
*-cargando (text: str):*

Simula un efecto de carga al imprimir caracteres con un breve retraso.
```python
def cargando(text: str):
    for i in text: 
        print(i, end="") 
        time.sleep(0.2) 
```
```mermaid 
flowchart TD;
    A[Inicio] --> B{¿Quedan caracteres?};
    B -->|Sí| C[Imprimir carácter con retraso];
    C --> B;
    B -->|No| D[Fin];
```
*-strToList(secuencia: str) -> list*

Convierte un string en una lista de caracteres para facilitar el análisis de datos.
```python
def strToList (secuencia : str) -> list:
    return list(secuencia)
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Convertir string en lista de caracteres];
    B --> C[Retornar lista];
    C --> D[Fin];
```
### Funciones de validación y comparación 
*-compareLengths(listR: list, listU: list) -> int*

Compara la longitud de la respuesta del usuario con respecto a la lista generada por el sistema, y si no coinciden, penaliza al usuario.
```python
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
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Comparar longitudes];
    B --> C{¿Son iguales?};
    C -->|Sí| D[Imprimir mensaje de éxito];
    D --> E[Retornar 0];
    C -->|No| F[Penalizar y mostrar mensaje];
    F --> G[Retornar -1];
    E & G --> H[Fin];
```
*-compareCapnoCap(listR: list, listU: list) -> tuple[int, bool]*

Esta función identifica los caracteres con capitalización correcta en la respuesta del usuario en comparación con la secuencia oculta y otorga los respectivos puntos.

```python
def compareCapnoCap (listR: list, listU : list) -> tuple[int, bool]:
    score : int = 0
    capU : list = []
    noCapU : list = []
    flagT : tuple = ()

    for i in listU:
        if i.isalpha() and i.isupper():
            capU.append(i)
        elif i.isalpha() and i.islower():
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
```
```mermaid 
flowchart TD;
    A[Inicio] --> B{¿Quedan caracteres?};
    B -->|Sí| C[Comparar mayúsculas y minúsculas];
    C --> D{¿Coinciden exactamente?};
    D -->|Sí| E[Añadir 2 puntos, marcar True];
    D -->|No| F{¿Coinciden sin importar mayúsculas?};
    F -->|Sí| G[Añadir 1 punto, marcar False];
    F -->|No| H[Imprimir mensaje neutro];
    E & G & H --> B;
    B -->|No| I[Retornar puntuación y flag];
    I --> J[Fin];
```
*-compare_index(user_chain: str, org_chain: str, score: int) -> tuple[int, bool]*

Esta función identifica los caracteres que coinciden en posición en ambas listas. 

```python
def compare_index(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    flagT : tuple = ()
    both_index = []
    bot = zip(org_chain, user_chain)
    both = list(bot)

    for org, user in both:
        if org == user:
            both_index.append(user)
        else:
            pass

    if len(both_index) == len(org_chain):
        flagT.append(True) 
    else:
        flagT.append(False) 
        match len(both_index):
            case 0:
                time.sleep(2)
                print("¿Que paso bb? ninguna esta en la posicion correcta ╥﹏╥")
            case 1:
                score += 1
                time.sleep(2)
                print (f"Parece que {str(both_index)} esta en la posicion correcta!!")
                print ("+ (1) punto")
            case _:
                for _ in both_index:
                    score += 1
                time.sleep(2)
                print (f"Parece que {str(both_index)} estan en la posicion correcta!!")
                print ("Que pilo eres ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
                print (f"+ ({len(both_index)}) puntos")

    if all.flagT() == True:
        flag = True 
    else:
        flag = False 
    return score, flag
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Inicializar lista de coincidencias];
    B --> C[Comparar caracteres de user_chain y org_chain];
    C --> D{¿Coinciden en posición?};
    D -->|Sí| E[Añadir carácter a lista];
    D -->|No| F[Continuar con siguiente carácter];
    E & F --> C;
    C --> G{¿Lista vacía?};
    G -->|Sí| H[Imprimir mensaje de fallo];
    G -->|No| I{¿Un solo acierto?};
    I -->|Sí| J[Incrementar score en 1];
    I -->|No| K[Añadir puntos según cantidad de aciertos];
    J & K --> L[Mostrar mensaje de puntos];
    L --> M[Retornar score y flag];
    M --> N[Fin];

```
*-compare_exist(user_chain: str, org_chain: str, score: int) -> tuple[int, bool]*

Evalúa qué caracteres de la entrada del usuario están presentes en la cadena correcta, sin importar la posición. 

```python
def compare_exist(user_chain:str, org_chain:str, score:int) -> tuple[int, bool]:
    flagT : tuple = ()
    in_both = []
    for char in user_chain:
        if char in org_chain:
            in_both.append(char)
        else:
            pass
        
    if len(in_both) == len(org_chain):
        flagT.append(True) 
    else:
        flagT.append(False) 
        match len(in_both):
            case 0:
                time.sleep(2)
                print("No le atinaste ni a una (ㆆ_ㆆ)")
            case 1:
                score += 1
                time.sleep(2)
                print (f"Parece que {str(in_both)} esta en la cadena!!")
                print ("+ (1) punto")
            case _:
                for _ in in_both:
                    score += 1
                time.sleep(2)
                print("( ͠❛ ₒ͠❛ ) ¿¿¿¿Te llamas Akinator????")
                print (f"Parece que {str(in_both)} estan en la cadena!!")
                print (f"+ ({len(in_both)}) puntos")

    if all.flagT() == True:
        flag = True 
    else:
        flag = False 
    return score, flag 
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Inicializar lista de coincidencias];
    B --> C[Recorrer caracteres de user_chain];
    C --> D{¿Está en org_chain?};
    D -->|Sí| E[Añadir carácter a lista];
    D -->|No| F[Continuar con siguiente carácter];
    E & F --> C;
    C --> G{¿Lista vacía?};
    G -->|Sí| H[Imprimir mensaje de fallo];
    G -->|No| I{¿Un solo acierto?};
    I -->|Sí| J[Incrementar score en 1];
    I -->|No| K[Añadir puntos según cantidad de aciertos];
    J & K --> L[Mostrar mensaje de puntos];
    L --> M[Retornar score y flag];
    M --> N[Fin];
```
### Funciones del juego 
*-history(name: str, score: int) -> dict*

Registra el nombre del jugador y su puntaje en un diccionario.
```python
def history(user_tries:list, name:str, score:int) -> dict:
    partida = {
        "Nombre" : name,
        "Puntaje" : score
    }
    user_tries.append(partida)
    
    user_tries.sort(key=lambda x: x["Puntaje"], reverse=True)

    for rank, dic in enumerate(user_tries, start= 1):
        dic["rank"] = rank

    user_tries_tab = tabulate(user_tries, headers= "keys", tablefmt= "grid")
    return user_tries_tab
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Crear entrada de usuario];
    B --> C[Añadir a lista de partidas];
    C --> D[Ordenar lista de intentos];
    D --> E[Asignar ranking];
    E --> F[Retornar tabla formateada];
    F --> G[Fin];
```
*game_start(configuration: dict)*

Maneja el flujo principal del juego, asegurando que se sigan las reglas configuradas.
```python
    def game_start(configuration:dict):
    if configuration.get("Lifes") == "infinitos":
        match configuration.values():
            case {"Data": "letras", "Repetition": "si", "Capital": "ambas"}:
                while win == False:
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]
            case {"Data": "letras", "Repetition": "no", "Capital": "ambas"}:
                while win == False:
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]

    if configuration.get("Lifes") in {3, 5, 10}:
        match configuration.values():
            case {"Data": "letras", "Repetition": "si", "Capital": "ambas"}:
                lifes = configuration.get("Lifes")
                for _ in range(lifes):
                    tuplaCapnoCap = compareCapnoCap(l_original, l_user)
                    score += tuplaCapnoCap[0]
                    flagCap = tuplaCapnoCap[1]
            case {"Data": "letras", "Repetition": "no", "Capital": "ambas"}:
                xxx
        if win == True:
            history(name, score)
```
```mermaid 
flowchart TD;
    A[Inicio] --> B{¿Vidas infinitas?};
    B -->|Sí| C[Seleccionar reglas adecuadas];
    B -->|No| D[Configurar intentos limitados];
    C & D --> E{¿Juego terminado?};
    E -->|No| F[Llamar funciones de validación y puntuación];
    F --> E;
    E -->|Sí| G[Mostrar resultado y terminar];
    G --> H[Fin];
```
*-validar_entrada(usuario_input: str, configuration: dict) -> bool*

Esta función se asegura de que en la respuesta del usuario solo haya caracteres permitidos por la configuración.
```python
def validar_entrada(usuario_input:str, configuration:dict) -> bool:
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

    if all(char in allowed_characters for char in usuario_input) == False : 
        validacion : bool = False
        cargando (". . .")
        print ("Mmm... \n")
        print ("¿No recuerdas como configuraste la partida?(ﾉಠдಠ)ﾉ︵┻━┻")
    else:
        validacion : bool = True
        cargando ("♥°˖✧°˖✧°˖✧°˖✧°˖✧◝(⁰▿⁰)◜✧˖°✧˖°✧˖°✧˖°♥")
    return validacion 
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Inicializar allowed_characters vacío];
    
    B --> C{¿Data permite letras?};
    C -->|Sí| D{¿Capital en mayúsculas?};
    D -->|Sí| E[Añadir mayúsculas a allowed_characters];
    D -->|No| F{¿Capital en minúsculas?};
    F -->|Sí| G[Añadir minúsculas a allowed_characters];
    F -->|No| H{¿Capital en ambas?};
    H -->|Sí| I[Añadir mayúsculas y minúsculas];

    C -->|No| J{¿Data permite números?};
    J -->|Sí| K[Añadir dígitos a allowed_characters];

    E & G & I & K --> L[Verificar si usuario_input contiene solo caracteres permitidos];
    
    L --> M{¿Todos los caracteres son válidos?};
    M -->|No| N[Imprimir mensaje de error y animación de carga];
    N --> O[Retornar False];
    
    M -->|Sí| P[Imprimir mensaje de éxito y animación de carga];
    P --> Q[Retornar True];

    O & Q --> R[Fin];

```
*-configuration_game(configuration: dict) -> dict*

Pide al usuario definir los parámetros con los que va a jugar, como el tipo de carácter, mayúsculas/minúsculas, repetición de caracteres, etc.
```python
def configuration_game(configuration:dict) -> dict: 
    while True:
        data_value = input("    1- Tipo de caracteres (letras, numeros, ambos): ")
        if data_value in {"letras", "numeros", "ambos"}:
            configuration["Data"] = data_value
            break
        else:
            print("No esta dentro de las opciones (⩺_⩹)")

    if configuration["Data"] == "letras" or configuration["Data"] == "ambos":
        while True:
            capital_value = input("    2- Capitalizacion de letras (mayusculas, minusculas, ambas): ")
            if capital_value in {"mayusculas", "minusculas", "ambas"}:
                configuration["Capital"] = capital_value
                break
            else:
                print("No esta dentro de las opciones (⩺_⩹)")
    else:
        pass
    
    while True:
        repetition_value = input("    3- Repetición de caracteres (si, no): ")
        if repetition_value == "si" or repetition_value == "no":
            configuration["Repetition"] = repetition_value
            break
        else:
            print("ಠ_ʖಠ ... si o no")
    
    while True:
        amount_value = int(input("    4- Cantidad de caracteres (3-10): "))
        if amount_value >= 3 and amount_value <= 10:
            configuration["Amount"] = amount_value
            break
        else:
            print("Puedes usar 3, 4, 5, 6 ... ಠ_ʖಠ ... 7, 8, 9, 10")

    while True:
        lifes_value = input("    5- Intentos (3, 5, 10, infinitos): ")
        if lifes_value in {3, 5, 10} or lifes_value :
            if lifes_value == "infinitos": 
                lifes_value = float('inf')
            else: 
                lifes_value = int(lifes_value)
            configuration["Lifes"] = lifes_value
            break
        else:
            print("Opcion NO disponible -(`෴´)- ")

    configuration_tab = tabulate(configuration.items(), tablefmt= "grid")

    return configuration_tab
```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Solicitar Tipo de caracteres];
    B --> C{¿Es válido?};
    C -->|No| B;
    C -->|Sí| D[Guardar elección en configuración];

    D --> E{¿Se eligieron letras o ambos?};
    E -->|Sí| F[Solicitar Capitalización];
    F --> G{¿Es válida?};
    G -->|No| F;
    G -->|Sí| H[Guardar elección en configuración];

    E -->|No| I[Omitir capitalización];

    H & I --> J[Solicitar Repetición de caracteres];
    J --> K{¿Es válida?};
    K -->|No| J;
    K -->|Sí| L[Guardar elección en configuración];

    L --> M[Solicitar Cantidad de caracteres];
    M --> N{¿Está en el rango 3-10?};
    N -->|No| M;
    N -->|Sí| O[Guardar elección en configuración];

    O --> P[Solicitar Intentos];
    P --> Q{¿Es válido?};
    Q -->|No| P;
    Q -->|Sí| R[Guardar elección en configuración];

    R --> S[Mostrar configuración con tabulate];
    S --> T[Retornar configuración];
    T --> U[Fin];
```
*-combinacion_aleatorea(configuration: dict) -> list*

Genera una cadena aleatoria basada en la configuración establecida.
```python
def combinacion_aleatorea(configuration:dict) -> list: 
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
 
    chain_list = []
    for elem in chain:
        chain_list.append(elem)

    return chain_list
```
```mermaid 
flowchart TD
    A["Inicio"] --> B["Inicializar lista de opciones"];
    
    B --> C{"¿Data es 'letras' o 'ambos'?"};
    C -->|Sí| D["Verificar capitalización"];
    
    D --> E{"¿Es 'mayúsculas'?"};
    E -->|Sí| F["Añadir mayúsculas a opciones"];
    E -->|No| G{"¿Es 'minúsculas'?"};
    G -->|Sí| H["Añadir minúsculas a opciones"];
    G -->|No| I["Añadir ambas a opciones"];
    
    C -->|No| J["Omitir letras"];
    
    F & H & I & J --> K{"¿Data es 'números' o 'ambos'?"};
    K -->|Sí| L["Añadir números a opciones"];
    K -->|No| M["Omitir números"];

    L & M --> N["Unir opciones en string"];
    N --> O["Obtener longitud de cadena"];

    O --> P{"¿Repetición permitida?"};
    P -->|No| Q["Usar random.sample para cadena única"];
    P -->|Sí| R["Usar random.choices para cadena con repetición"];

    Q & R --> S["Convertir cadena en lista"];
    S --> T["Retornar lista"];
    T --> U["Fin"];

```
## Función principal 
*-if __name__ == "__main__":*

La función main gestiona el flujo del juego, permite al usuario interactuar con las configuraciones del juego, y evalúa su desempeño , mientras controla las vidas y el puntaje.
```python
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
        elif win == True:
            functionality_defs.cargando("GANASTEEEEEEEEEEEEEEEEE")

        # Al terminar la partida, pregunta al usuario si quiero jugar otravez
        dead = input("¿Quieres jugar otra vez?: ")
        if dead == "si":
            functionality_defs.history("\n", name, score) # Mostrar leaderboard
        elif dead == "no":
            break
    functionality_defs.history("\n", name, score)
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━┓\n♡   Gracias por jugar   ♡\n┗━━━━━━━━━━━━━━━━━━━━━━━┛""")

```
```mermaid 
flowchart TD;
    A[Inicio] --> B[Mostrar bienvenida]
    B --> C[Solicitar nombre al usuario]
    C --> D[Mostrar preguntas y configuracion]
    D --> E[Generar secuencia aleatoria]
    E --> F[Ocultar secuencia con asteriscos]
    F --> G[Solicitar secuencia de usuario]
    G --> H[Convertir secuencia de usuario a lista]
    H --> I[Comparar secuencias y calcular puntaje]
    I --> J{¿Entrada inválida o configuración incorrecta?}
    J -->|Sí| G
    J -->|No| L{¿Secuencia correcta?}
    L -->|No| M[Iniciar partida]
    L -->|Sí| N[Fin del juego]
    M --> O{¿Lifes infinitos?}
    O -->|Sí| P[Iniciar juego con reglas infinitas]
    O -->|No| Q{¿Lifes 3, 5, 10?}
    Q -->|Sí| R[Iniciar juego con reglas de vidas limitadas]
    Q -->|No| N
    P --> T[Comparar secuencias y calcular puntaje]
    T --> U{¿Juego ganado?}
    U -->|Sí| V[Mostrar mensaje de victoria]
    V --> N
    U -->|No| W[Mostrar mensaje de derrota]
    R --> T
    W --> X{¿Reintentar juego?}
    X -->|Sí| Y[Registrar puntaje y continuar]
    X -->|No| Z[Mostrar agradecimiento y salir]
    Y --> B
    Z --> N
    

```

***
---
## Instalación de R4nd.M1n1ng

Sigue estos pasos para instalar y ejecutar el juego en tu sistema.

###  Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- *Python 3.8 o superior* 
  Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

- *Pip (gestor de paquetes de Python)* 
  Para verificar si lo tienes instalado, ejecuta:  
  ```bash
  pip --version
  ```
### Instalación 
1. Clona el repositorio o descarga el código fuente.
 ```bash
 git clone https://github.com/tu-usuario/R4nd.M1n1ng.git
 cd R4nd.M1n1ng
 ```
2. Instala las dependencias necesarias.

### Ejecución 
Para iniciar el juego, usa el siguiente comando dentro del directorio del proyecto: 
```bash
- python main.py
```
***
## Colaboradores:
* Juan Manuel Dávila Dominguez
* Zaida Alejandra Guzman Martínez
* Laura Mariana de Jesús García Garnica
***
## Referencias
* https://labex.io/es/tutorials/python-how-to-implement-time-delays-in-python-420943
* https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
* https://www.reddit.com/r/learnpython/comments/qa1g75/how_to_print_one_character_at_a_time_slowly_in/?rdt=52729
* https://stackoverflow.com/questions/71034827/python-match-case-using-dictionary-keys-and-values
