diccionario = {
    "nombre": "ulises", #0
    "apellido" : "palacio", #1
    "subs": 100000 #2
}

claves = diccionario.keys();#devuevle las claves tambien nos sirve para iterar

valor_de_un_elemento  = diccionario.get("subs")#obteniendo un elemento con get() si no encuentra nada  el programa continua

#eliminando todo del diccionario

#diccionario.cler();

#eliminando un elemento del diccionario  siq queres eliminar mas de uno poner una coma y el otro elemento 




diccionario.pop("apellido");

#obteniendo un elemento dict_items iterable

diccionario_iterable = diccionario.items()




print(diccionario_iterable)