#PUZLE LINEAL CON BUSQUEDA EN AMPLITUD    //hacer con profundidad  (ver nodos visitados,)
from arbol import Nodo
def Busqueda_en_Amplitud(estado_inicial,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial=Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while(not solucionado) and len(nodos_frontera)!=0:
        nodo=nodos_frontera.pop(0)
        #Extrae nodo y añade a los visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos()==solucion:
            #solucion encontrada
            solucionado =True
            return nodo
        else:
            #expandir nodos hijo
            dato_nodo=nodo.get_datos()
            #operador izquierdo
            hijo=[dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3]]
            hijo_izquierdo=Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
            #operacdor central
            hijo=[dato_nodo[0],dato_nodo[2],dato_nodo[1],dato_nodo[3]]
            hijo_central= Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados)\
                and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            #operador derecho
            hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2]]
            hijo_derecho=Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados)\
                and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
            nodo.set_hijos([hijo_izquierdo,hijo_central,hijo_derecho])


if __name__ == "__main__":
    estado_inicial=['a','c','d','b']
    solucion=['a','b','c','d']
    nodo_solucion=Busqueda_en_Amplitud(estado_inicial,solucion)
    #mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre()!=None:
        resultado.append(nodo.get_datos())
        nodo=nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado) 

