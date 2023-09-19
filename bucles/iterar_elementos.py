

animales = ["gato","perro","loro","cocodrilo"];
numeros = [12,15,22,34];

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a : {animal}");


#recorriendo la lista numeros y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero*10;
    print(resultado);    



#iteramos dos listas del mismo tamaño al mismo tiempo

for numero,animal in zip(animales,numeros):
    print(f"recorriendo la lista1:{numero}");
    print(f"recorriendo la lista1:{animal}");

#forma no optima de recorer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0] # recorro el indice
    valor = num[1]#recorro sus valores
    print(f'el ìndice es: {indice} y el valor es: {valor}')


#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else: 
    print("el bucle termino" )
    
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos