# REALIZAR UN PROGRAMA EN PYTHON PARA LEER DESDE TECLADO UNA CADENA.
# DETERMINAR SI ESA CADENA ES PALINDROMO
#EJEMPLO: OSO, ANA, BOB, ADIDA


def palindromo():
    cadena = str(input("Ingrese la palabra para comprobar si es palindromo : "))
    lista=[]
    for a in cadena :
        lista.append(a)
    
    lista.reverse()
    
    palabra_reversa=""

    for a in lista:
        palabra_reversa=palabra_reversa+a

    print(palabra_reversa)
    if cadena==palabra_reversa:
        print("palabra palindroma")
    else:
        print("palabra no palindroma")


def palindromo2():
    palabra=input("Introduzca una palabra : ")
    acumulador=""

    for i in palabra:
        acumulador=i+acumulador
    
    if acumulador==palabra:
        print("OK")
    else:
        print("NO")





if __name__ == '__main__':
    palindromo2()




