"""
sintaxis de la funcion range():
range(inicio,final[paso])
si no hay inicio por defecto es 0 y el paso por defecto es 1 cuando no se indica
la funcion genera una serie de enteros entre el inicio y el fin -1 con un incremento dado por el paso
"""
#caso 1: range(fin)
print(list(range(3)))
# caso 2: range (inicio,fin)
print(list(range(20,30)))
#caso 3: range(inicio,fin,paso)
print(list(range(0,-10,-2)))
