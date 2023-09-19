#List crea una lista

lista = list([25])


#el len nos devuelve la cantidad de elementos que tiene una lista 
cantidad_elementos = len(lista);


#agrega un elemento a la lista

lista.append(23);



#agregando un elemento a la lista con un indice especifico 

lista.insert(0,"toma mama")


#agregando varios elementos a la lista

lista.extend([5,55])#le pasamos una lista para agregar otra lista


#eliminando un elemento de la lista por su indice 

lista.pop(0);#al poner -1 eliminamos el ultimo elemento de la lista 

#removiendo elemento de la lista por su valor

#lista.remove()


#eleminando todos los elementos de la lista
#lista.clear

#ordena los elemetntos de la lista de forma ascendente solo si son numeros
lista.sort(reverse=True)#dentro de los parentesis se les puede agregar el reverse=True y lo ordena al reves


#invirtiendo los elemetos de una lista 

lista.reverse()


print(lista);