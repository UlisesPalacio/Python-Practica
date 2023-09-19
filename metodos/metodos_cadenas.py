cadena_1 = "hola mi nombre es Ulises"
cadena_2 = "bienvenido a python"

#metodos el dato.el_nombre_del_metodo() son funciones especificas de objetos

resultado2= cadena_1.upper()#este metodo comvierte texto a mayuscula 

resultado3= cadena_1.lower()#este metodo comvierte texto a minuscula 

resultado3= cadena_1.capitalize()#este metodo comvierte todo a minuscula y despues comvierte la  primera letra a mayuscula 


#buscamos una cadena en otra cadena 

busqueda_find = cadena_1.find("mi") #encuentra la pocicion de la primer letra de la palabra que buscamos 
                                    #cuando no encuentra un valor retorna -1

#buscamos una cadena en otra cadena

busqueda_index = cadena_1.index("mi")# es como la anterior pero si no encuentra nos devuelve un error (excepcion)


#si es numerico devolvemos true sino devolvemos false

es_numerico = cadena_1.isnumeric()#verifica si es un numero aunque este con comillas


#si es alfanumerico devolvemos true sino devolvemos false

es_alfanumerico = cadena_1.isalpha();#solo si es alfanumerico el metodo es true


#buscamos una cadena en otra cadena ,devuelve la cantidad de veces que coincida

conta_coincidencias = cadena_1.count("i")#muestra la cantidad cuantas veces aparece la letra i sino encuentra nos muestra 0


#len funcion no metodo  contamos cuantos caracteres tiene una cadena 

contar_caracteres = len(cadena_1);


#verificamos si una cadena empieza con otra cadena dada , si es asi devuelve true

empieza_con = cadena_1.startswith("h")

#verificamos si una cadena termina con otra cadena dada , si es asi devuelve true

termina_con = cadena_1.endswith("h")


#reemplazamos una cadena dada por otra dada 
#si el valor 1 se encuentra en la cadena original reemplaza el valor 1 de la misma por el valor 2

cadena_nueva = cadena_1.replace("ho","ha"); #primer parametro es el valor anterior y el otro es el que vamos a usar ahora


#separar cadenas con la cadena que le pasemos

cadena_separada = cadena_1.split(" ");#este metodo crea una lista  separada ejemplo de recien
                                    #separe el texto hola mi nombre es Ulises con un espacio y me quedo asi
                                    #['hola', 'mi', 'nombre', 'es', 'Ulises']



print(type(cadena_separada))

