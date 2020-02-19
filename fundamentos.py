print("Hola mundo")
# Estructura IF
# Operadores
# > Mayor
# < Menor
# != Diferente
# == Igual

# IDENTACION Y CONDICIONAL IF


# input('mensaje) devuelve un string haci que lo transformamos a int
x = int(input("Ingrese un numero: "))
if (x % 2) == 0:
    print("Numero Par")
else:
    print("Numero Impar")


# Bucle for
for i in range(10):  # range(de cero hasta el valor especificado)
    print(i)

for i in range(4, 10):  # range(valor inicial, valor final)
    print(i)

for i in range(4, 10, 2):  # range(valor inicial , valor final, numero de incrementos 'de dos en dos', 'tres en tres', etc)
    print(i)

# BUCLE WHILE
x = 1
bandera = True
while(bandera):
    print(x)
    x = x+1
    if x == 3:
        bandera = False


# CASE
x = 9
if x == 1:
    print('Lunes')
elif x == 2:
    print('Martes')
elif x == 3:
    print('Miercoles')
else:
    print("Dia no existe")


# LISTAS
l1 = [1, 2, 3, "Numero", 0]

l1.append(32)  #asi se agregan elemtos a la lista con 'append(nuevo dato)'
l1.pop()  #asi sacamos el ultimo elemento de la lista con 'pop'


for a in l1:  # Recorremos la lista con un for
    print(a)

# Tuplas
# en una tupla no se pueden modificar los valores definidos en el princio
t1 = (1, 2, 3, 4, 5)
# t1[1]=10 no se puede hacer esto en una tupla

# Coleccion
c1 = {"uno": 1, "dos": 2, "tres": 3}

# Entradas desde el teclado
nombre = input("Introduzca un dato ")
year = int(input("Cual es su edad "))
print(nombre, "Su edad es: ", year*2)
