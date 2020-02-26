

def frase_palindromo():
    # Ejemplos "Dabale arroz a la zorra el abad", "Salta Lenín el atlas" , "Amigo, no gima",
    # "Atale, demoníaco Caín, o me delata", "Anás usó tu auto, Susana", "A Mercedes, ése de crema",
    # "A mamá Romale aviva el amor a papá, y a papá Roma le aviva el amora mamá" ,"!arriba la birra¡" ,
    frase = input("Ingrese una frase para comprobar si es palindroma : ").lower()
    frase = frase.replace(" ", "")
    frase = frase.replace(",", "")

    acumulador = ""
    frase_estandarizada = ""

    for i in frase:
        acumulador = convertir_letras(i)+acumulador
        if i != "!" and i != "¡" and i != "¿" and i != "?":
            frase_estandarizada = frase_estandarizada+convertir_letras(i)
        else:
            frase_estandarizada = frase_estandarizada+i

    if acumulador == frase_estandarizada:
        print("Palindromo")
    else:
        print("No Palindromo")


def convertir_letras(letra):
    try:
        letras = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
                  "!": "¡", "¡": "!", "¿": "?", "?": "¿", "ü": "u"}
        return letras[letra]
    except KeyError:
        return letra


if __name__ == '__main__':
    frase_palindromo()
