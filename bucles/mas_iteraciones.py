#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "hola ulises"
numeros = [2,5,8,10]



#evitando que se coma una granada con la sentencia continue 
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer {fruta}");
    

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
else: 
    print("terminado")



for letra in cadena :
    print(letra);

#for en una sola linea de còdigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)