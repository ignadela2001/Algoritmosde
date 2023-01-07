lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar (l):
    l = list(set(l))
    l.sort(reverse=True)
    for i,n in enumerate(l):
        if n%2 != 0:
            del (l[i])
            
    suma = sum(l)
    l.insert(0, suma)
    return l

nueva_lista = modificar(lista)
print (nueva_lista[0]  == sum(nueva_lista[1:]))

            
    
    
