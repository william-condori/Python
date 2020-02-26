def comprobarDiscriminante(a, b, c):
    discriminante = (b**2)-4*a*c
    if discriminante == 0:
        obtenerX1(a, b, c)
    elif discriminante > 0:
        obtenerX1(a, b, c)
        obtenerX2(a, b, c)
    else:
        print('Numeros imaginarios')


def obtenerX1(a, b, c):
    try:
        x1 = (-b-((b**2)-4*a*c)**(1/2))/(2*a)
        mostrarX1(x1)
    except ZeroDivisionError:
        print('No se puede dividir por cero')


def obtenerX2(a, b, c):
    try:
        x2 = (-b+((b**2)-4*a*c)**(1/2))/(2*a)
        mostrarX2(x2)
    except ZeroDivisionError:
        print('No se puede dividir por cero')


def mostrarX1(x1):
    print("valor de x1 = {}".format(x1))

def mostrarX2(x2):
    print("valor de x2 = {}".format(x2))
    


def pedirDatos():
    while True:
        try:
            a = float(input("Ingrese el valor de a "))
            b = float(input("Ingrese el valor de b "))
            c = float(input("Ingrese el valor de c "))
            comprobarDiscriminante(a, b, c)
        except ValueError:
            print("Los datos deben ser enteros!!!!")

        intentar=input('''Desea volver a intentarlo?
                                [s]i
                                [n]o 
                          : ''')
        if intentar =="n":
            break
      

if __name__ == '__main__':
    print("-----------------------------------------------------")
    print("|     CALCULADORA DE ECUACIONES CUADRATICAS         |")
    print("-----------------------------------------------------")
    pedirDatos()
