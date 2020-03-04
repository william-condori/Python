#PUZLE LINEAL CON BUSQUEDA EN AMPLITUD    //hacer con profundidad  (ver nodos visitados,)
from arbol import Nodo
def Busqueda_en_Amplitud(estado_inicial,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial=Nodo(estado_inicial)
    #nodos_frontera.append(nodoInicial)
    nodoTemporal=[]
    nodoTemporal.append(nodoInicial)


    while(not solucionado) and len(nodoTemporal)!=0:
        nodo=nodoTemporal.pop()
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
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodoTemporal):
                nodos_frontera.append(hijo_izquierdo)
            #operacdor central
            hijo=[dato_nodo[0],dato_nodo[2],dato_nodo[1],dato_nodo[3]]
            hijo_central= Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodoTemporal):
                nodos_frontera.append(hijo_central)

            #operador derecho
            hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2]]
            hijo_derecho=Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodoTemporal):
                nodos_frontera.append(hijo_derecho)
            nodo.set_hijos([hijo_izquierdo,hijo_central,hijo_derecho])
            for nodoAux in range(len(nodos_frontera)):
                nodoTemporal.append(nodos_frontera.pop())


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

