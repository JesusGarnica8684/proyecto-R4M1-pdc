import random
import string

configuracion = {
    "Tipo" : "",
    "Capitalizacion" : "",
    "Repeticion" : "",
    "Cantidad" : "",
    "Vidas" : ""
}

def combinacion_aleatorea(configuracion:dict, lon:int):
    opciones = []
    mayus = string.ascii_uppercase # Mayusculas
    minus = string.ascii_lowercase # Minusculas
    mayus_minus = string.ascii_letters # Ambas
    nume = string.digits # Numeros
    if configuracion["Tipo"] == "numeros" or configuracion["Tipo"] == "ambos":
        opciones.append(nume)
    else:
        pass

    if configuracion["Tipo"] == "letras" or configuracion["Tipo"] == "ambos":
        opciones.append(nume)
        match configuracion["Capitalizacion"]:
            case "mayusculas":
                opciones.append(mayus)
            case "minusculas":
                opciones.append(minus)
            case "ambas":
                opciones.append(mayus_minus)
    else:
        pass
    opciones_string = "".join(opciones)

    if configuracion["Repeticion"] == "no":
        cadena = "".join(random.sample(opciones_string, lon))
    else:
        cadena = "".join(random.choices(opciones_string, lon))
    
    respuesta_lista = []
    for i in range(len(cadena)):
        respuesta_lista.append(i)
    return respuesta_lista