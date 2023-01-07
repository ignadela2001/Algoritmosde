

def imprime_valores(lista):

    for valor in lista:

        if valor > 300:
            break;
        
        if (valor % 10 == 0) and (valor < 200):
            print("numero {}".format(valor))


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Llamada recurvida a cada mitad
        mergeSort(left)
        mergeSort(right)

        # Dos iteradores para recorrer las dos mitades
        i = 0
        j = 0
        
        # Iterador para la lista principal
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # Se usa el valor de la mitad izquierda
              myList[k] = left[i]
              # Movemos el iterador a delate
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Movemos al siguiente hueco
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


mi_lista=[18, 50, 210, 80, 145, 333, 70, 30]

print("lista inicial")
print(mi_lista)
print()
print("Funcion imprime_valores")
print()

imprime_valores(mi_lista)

print()

mergeSort(mi_lista)

print("lista ordenada")
print(mi_lista)

print()
print("Funcion imprime_valores")
print()


imprime_valores(mi_lista)

