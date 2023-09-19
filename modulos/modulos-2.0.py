#si el modulo estuviera dentro de una carpeta en la misma ruta 
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("C:\\Users\\Usuario\\Desktop\\PYTHON\\funciones_buenas")

import saludar as modulo_saludo


print(sys.path)
print(modulo_saludo.saludar("Dalto"))
# \ barra invertida es con alt gr + ?
