


lista=[7,8,9,10,14,13]

def estaOrdenada(lista):
    return lista == sorted(lista)

resultado = estaOrdenada(lista)

if resultado:
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")