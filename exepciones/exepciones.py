#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True: 
        #pidiendo numeros
        a = input("numero 1 : ");
        b = input("numero 2 : ");
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b);
        #si lanzo una excepción, pedirle que reingrese los datos    
        except ValueError as e:
            print("no es un numero intenta ingresar de nuevo")
            print(f"ERROR: {e}")
        #si todo salio bien terminamos el bucle    2
        else:
            break;
        #el finally se ejecuta siempre
        finally: 
            print("Esto se ejecuta siempre")
    
    #mostrando el resultado
        
    return resultado;
print(sumar_dos());