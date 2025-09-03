# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacioón del DataFrame
df_alumnos = pd.DataFrame(datos)

# Cálculo del promedio de las notas
Notas = ['Nota1', 'Nota2', 'Nota3']

# Creación de la nueva columna 'promedio' con el promedio de las notas
df_alumnos['Promedio'] = df_alumnos[Notas].mean(axis=1).round(1) # axis=1 es para calcular el promedio por fila

#print(df_alumnos)

# Ordenar en la columna 'Promedio' de mayor a menor
df_alumnos_aordenados = df_alumnos.sort_values('Promedio', ascending=False)

print(df_alumnos_aordenados)