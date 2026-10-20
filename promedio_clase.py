"""
un profesor necesita bun progrma que le ayude a calcular el promedio de la clase 
el ingresa el nombre y el valor de la nota final de cada estudiante estudiante (cada nota es de 0 a 5)
al final necesita saber cual es el mejro estudiante y el promedio de todo el curso
"""
cantidad=int(input("cantidad de estudiantes: "))
mejor_es=""
nota_mayor=0.0
promedio=0.0
suma=0
for veces in range(1,cantidad+1):
    print("estudiante # ",veces)
    nombre=input("nombre del estudiante: ")
    nota=float(input("nota del estudiante"))
    suma= suma +nota
    if nota>nota_mayor:
        nota_mayor=nota
        mejor_es=nombre
promedio=suma/cantidad
print("el promedio del curso es ",promedio)
print("el mejor estudiante es ",mejor_es," con nota de ",nota_mayor)