import itertools
def combinatoria2(set,num_combinaciones):
    permutaciones = itertools.combinations(set, num_combinaciones)
    lista_permutaciones = []    
    for elemento in permutaciones:
        lista_permutaciones.append(elemento)  
    print (lista_permutaciones)
